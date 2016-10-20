from django.apps import AppConfig


class AccountsConfig(AppConfig):
	name = 'apps.accounts'
	verbose_name = 'Accounts'

	def ready(self):
		pass
