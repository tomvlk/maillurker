import asyncore
import smtpd
import email
import logging
import threading
from time import sleep

from django.conf import settings
from django.db import transaction

from apps.mails import models

logger = logging.getLogger(__name__)


class Lurker(smtpd.SMTPServer):
	INSTANCE = None
	THREAD = None

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
				subject=msg.get('Subject'),
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

		return

	@staticmethod
	def parse_addresses(raw):
		"""
		Parse Addresses
		:param raw:
		:return:
		"""
		if type(raw) is not list:
			raw = [raw]

		return email.utils.getaddresses(raw)

	@staticmethod
	def parse_address(raw):
		"""
		Parse Address
		:param raw:
		:return:
		"""
		return list(email.utils.parseaddr(raw))


	@staticmethod
	def start(test=False, threaded=False):
		"""
		Start SMTP catcher.

		:param test:
		:param threaded:
		:return:
		"""
		if Lurker.INSTANCE:
			return

		Lurker.INSTANCE = Lurker((settings.SMTPD_ADDRESS, settings.SMTPD_PORT), None)

		if threaded:
			Lurker.THREAD = threading.Thread(target=asyncore.loop, kwargs={'timeout': 1})
			Lurker.THREAD.start()
			# Sleep to make sure our Lurker instance is ready.
			sleep(3)

		logger.info('Started listening on {}:{}'.format(settings.SMTPD_ADDRESS, settings.SMTPD_PORT))

	@staticmethod
	def stop():
		"""
		Stop threaded server.
		:return:
		"""
		Lurker.INSTANCE.close()
		if Lurker.THREAD:
			Lurker.THREAD.join()
