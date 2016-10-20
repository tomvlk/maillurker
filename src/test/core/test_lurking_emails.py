from ..base import TestCase

from apps.mails import models
from test.eml import send_eml


class MessageModelsTestCase(TestCase):
	def test_simple_mixed_email(self):
		sended = send_eml(
			path='complicated-message.eml',
			from_addr='foo@bar.com',
			to_addrs='Manuel Lemos <example@linux.local>'
		)

		self.assertTrue(sended)

		message = models.Message.objects.last()
		self.assertIsInstance(message, models.Message)

		self.assertEqual(message.subject, 'Testing MIME Messag')
		self.assertEqual(message.parts.count(), 8)
