from django.apps import AppConfig

from apps.core.menu import Menu, Item


class MailsConfig(AppConfig):
	name = 'apps.mails'
	verbose_name = 'Mails'

	def ready(self):

		Menu.add_item(Item(
			name='mails',
			label='Mails',
			route_name='mails:list',
			active_regex='^(/mails/)$',
		))
