import asyncore

from django.core.management import BaseCommand

from apps.core.smtpd import Lurker


class Command(BaseCommand):
	help = 'Start the SMTP Lurking server.'

	def handle(self, *args, **options):
		Lurker.start()

		try:
			asyncore.loop()
		except KeyboardInterrupt:
			exit()
