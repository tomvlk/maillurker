from django.apps import AppConfig


class MailsConfig(AppConfig):
	name = 'apps.mails'
	verbose_name = 'Mails'

	def ready(self):
		pass
