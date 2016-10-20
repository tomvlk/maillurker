import asyncore
from random import Random

from faker import Factory

from django.conf import settings
from django.core.management import BaseCommand

from apps.core.smtpd import Lurker
from test.eml import send_eml

fake = Factory.create('en_GB')


class Command(BaseCommand):
	help = 'Spoof the lurker with some emails.'

	def add_arguments(self, parser):
		parser.add_argument('server', nargs='*', type=str, default='127.0.0.1',
							help='Server to send to.')
		parser.add_argument('port', nargs='*', type=int, default='1025',
							help='Server port to send to.')

		parser.add_argument('-i', '--iterations', type=int, default=50, dest='iterations',
							help='Number of fake data to spoof.')

	def handle(self, *args, **options):
		server = options['server']
		port = options['port']
		iterations = options['iterations']

		for _ in range(0, iterations):
			body_file = Random().randint(1, 6)
			send_eml(
				server=server, port=port,
				path='random/{}.eml'.format(body_file),
				from_addr=fake.company_email(),
				to_addrs='{} <{}>'.format(fake.name(), fake.email()),
			)
