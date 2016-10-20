import os

from ..base import TestCase

from apps.core.smtpd import Lurker
from apps.mails import models
from test.eml import send_eml


class MessageModelsTestCase(TestCase):
	def test_simple_emails(self):
		sended = send_eml(
			path='complicated-message.eml',
			from_addr='foo@bar.com',
			to_addrs='Manuel Lemos <example@linux.local>'
		)

		self.assertTrue(sended)

		print(models.Message.objects.all())
