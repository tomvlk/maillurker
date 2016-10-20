from django.test import TestCase as DjangoTestCase

from apps.core.smtpd import Lurker


class TestCase(DjangoTestCase):

	def setUp(self):
		Lurker.start(test=True, threaded=True)

	def tearDown(self):
		Lurker.stop()
