import asyncore
import base64
import smtpd
import email
import logging
import threading
from email.header import decode_header
from time import sleep

from django.conf import settings
from django.core.cache import cache
from django.db import transaction

from apps.mails import models

logger = logging.getLogger(__name__)


class Lurker(smtpd.SMTPServer):
	INSTANCE = None
	THREAD = None
	CLEANER = None

	enable_SMTPUTF8 = True

	def process_message(self, peer, mailfrom, rcpttos, data, **kwargs):
		"""
		Process and save message

		:param peer:
		:param mailfrom:
		:param rcpttos:
		:param data:
		:param kwargs:
		:return:
		"""
		msg = email.message_from_string(data)
		sender = self.parse_address(msg.get('From'))

		# Start transaction of inserting message and parts.
		with transaction.atomic():
			# Create message
			message = models.Message.objects.create(
				peer=peer[0],
				port=peer[1],
				headers=dict(msg.items()),
				sender_name=sender[0],
				sender_address=sender[1],
				recipients_to=self.parse_addresses(msg.get_all('To', [])),
				recipients_cc=self.parse_addresses(msg.get_all('Cc', [])),
				recipients_bcc=self.parse_addresses(msg.get_all('Bcc', [])),
				subject=Lurker.clean_international_string(msg.get('Subject')),
				source=data,
				size=len(data),
				type=msg.get_content_type(),
			)

			# Create parts
			for part in msg.walk():
				body = part.get_payload(decode=True)
				length = len(body) if body else 0

				models.MessagePart.objects.create(
					message=message,
					is_attachment=part.get_filename() is not None,
					filename=part.get_filename(),
					type=part.get_content_type(),
					charset=part.get_content_charset(),
					body=body,
					size=length
				)

		try:
			self.clear_cache()
		except Exception as e:
			logger.debug('Cache clearance failed.')
			logger.debug(e)

		logger.info(
			'Saved email from \'{}:{}\' with {} parts.'.format(message.peer, message.port, message.parts.count())
		)

		return

	@staticmethod
	def clear_cache():
		if settings.DEBUG:
			return

		cache.delete_many([
			'mails.context.counts',
		])

	@staticmethod
	def clean():
		num_deleted = models.Message.cleanup()

		if num_deleted > 0:
			logger.info('Cleanup deleted \'{}\' old messages.'.format(num_deleted))

		# Schedule next cleanup task.
		Lurker.CLEANER = threading.Timer(3600, Lurker.clean)
		Lurker.CLEANER.start()

	@staticmethod
	def clean_international_string(entry):
		# Remove the prefix and suffix if exists.
		prefix = '=?UTF-8?B?'
		suffix = '?='

		if prefix in entry and suffix in entry:
			middle = entry[len(prefix):len(entry)-len(suffix)]
			decoded = base64.b64decode(middle)
			return decoded.decode('utf-8')
		return entry

	@staticmethod
	def parse_addresses(raw):
		"""
		Parse Addresses
		:param raw:
		:return:
		"""
		if type(raw) is not list:
			raw = [raw]

		addresses = list()

		for entry in raw:
			addresses.append(Lurker.clean_international_string(entry))

		return email.utils.getaddresses(addresses)

	@staticmethod
	def parse_address(raw):
		"""
		Parse Address
		:param raw:
		:return:
		"""
		return list(email.utils.parseaddr(Lurker.clean_international_string(raw)))

	@staticmethod
	def start(test=False, threaded=False, cleaner=False):
		"""
		Start SMTP catcher.

		:param test:
		:param threaded:
		:param cleaner:
		:return:
		"""
		if Lurker.INSTANCE:
			return

		Lurker.INSTANCE = Lurker((settings.SMTPD_ADDRESS, settings.SMTPD_PORT), None)

		if cleaner:
			Lurker.CLEANER = threading.Timer(3600, Lurker.clean)
			Lurker.CLEANER.start()

		if threaded:
			Lurker.THREAD = threading.Thread(target=asyncore.loop, kwargs={'timeout': 1})
			Lurker.THREAD.start()
			# Sleep to make sure our Lurker instance is ready.
			sleep(2)

		logger.info('Started listening on {}:{}'.format(settings.SMTPD_ADDRESS, settings.SMTPD_PORT))

		if cleaner:
			logger.info('Scheduled cleaner task in background.')

	@staticmethod
	def stop():
		"""
		Stop threaded server.
		:return:
		"""
		Lurker.INSTANCE.close()
		if Lurker.CLEANER:
			Lurker.CLEANER.cancel()

		if Lurker.THREAD:
			Lurker.THREAD.join()
