import asyncore

from django.conf import settings
from django.core.management import BaseCommand

from apps.core.smtpd import Lurker


class Command(BaseCommand):
	help = 'Start the SMTP Lurking server.'

	def add_arguments(self, parser):
		parser.add_argument(
			'--no-cleanup', dest='cleaner', action='store_false',
			help='Don\'t start cleanup if settings has entry for it. (Override settings).'
		)

		parser.set_defaults(cleaner=True)

	def handle(self, *args, **options):
		cleaner = settings.CLEANUP
		if not options['cleaner']:
			cleaner = False

		Lurker.start(cleaner=cleaner)

		try:
			asyncore.loop()
		except KeyboardInterrupt:
			Lurker.stop()
			exit()
