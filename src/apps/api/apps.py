from django.apps import AppConfig


class ApiConfig(AppConfig):
	name = 'apps.api'
	verbose_name = 'API'

	def ready(self):
		pass
