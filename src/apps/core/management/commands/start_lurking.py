import asyncore

from django.conf import settings
from django.core.management import BaseCommand

from apps.core.smtpd import Lurker


class Command(BaseCommand):
	help = 'Start the SMTP Lurking server.'

	def handle(self, *args, **options):
		lurker = Lurker.start()

		self.stdout.write(self.style.WARNING('Started lurking on {}:{}..'.format(
			settings.SMTPD_ADDRESS, settings.SMTPD_PORT
		)))

		asyncore.loop()
