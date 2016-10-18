from django.test import TestCase

from apps.core.smtpd import Lurker
from apps.mails import models


class MessageModelsTestCase(TestCase):
	def setUp(self):
		pass

	def test_message_creation(self):
		message = models.Message.objects.create(
			peer='127.0.0.1',
			port='1555',
			sender_name='Example Sender',
			sender_address='example@sender.com',
			recipients_to=Lurker.parse_addresses(['Test <test@receiver.com>']),
			recipients_cc=Lurker.parse_addresses([]),
			recipients_bcc=Lurker.parse_addresses([]),
			headers={},
			subject='Subject',
			source='Sample Body'.encode(),
			size=len('Sample Body'),
			type='text/plain',
		)

		self.assertIsInstance(message, models.Message)

		message.delete()

		self.assertIsNone(message.pk)
