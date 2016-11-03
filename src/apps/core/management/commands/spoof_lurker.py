import os
import glob

from random import Random

from django.conf import settings
from faker import Factory
from django.core.management import BaseCommand
from test.eml import send_eml

fake = Factory.create('en_GB')


class Command(BaseCommand):
	help = 'Spoof the lurker with some emails.'

	def add_arguments(self, parser):
		parser.add_argument('-t', '--type', nargs='*', type=str, choices=('random', 'examples'),
							help='Type of messages.')

		parser.add_argument('server', nargs='*', type=str, default='127.0.0.1',
							help='Server to send to.')
		parser.add_argument('port', nargs='*', type=int, default='1025',
							help='Server port to send to.')

		parser.add_argument('-i', '--iterations', type=int, default=50, dest='iterations',
							help='Number of fake data to spoof.')

	def handle(self, *args, **options):
		message_type = options['type']
		server = options['server']
		port = options['port']
		iterations = options['iterations']

		if 'random' in message_type:
			for _ in range(0, iterations):
				body_file = Random().randint(1, 6)
				send_eml(
					server=server, port=port,
					path='random/{}.eml'.format(body_file),
					from_addr=fake.company_email(),
					to_addrs='{} <{}>'.format(fake.name(), fake.email()),
				)

		elif 'examples' in message_type:
			mail_path = os.path.join(settings.TEST_DIR, 'files', 'eml')

			for file in glob.iglob(os.path.join(mail_path, '*', '*.eml'), recursive=True):

				to_addresses_count = Random().randint(1, 4)
				to_addresses = list()
				for _ in range(0, to_addresses_count):
					to_addresses.append('{} <{}>'.format(fake.name(), fake.email()))

				try:
					send_eml(
						server=server, port=port,
						path=file,
						from_addr=fake.company_email(),
						to_addrs=', '.join(to_addresses)
					)
				except Exception as e:
					print('Exception: ', e)
