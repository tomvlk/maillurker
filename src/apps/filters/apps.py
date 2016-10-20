from django.apps import AppConfig


class FiltersConfig(AppConfig):
	name = 'apps.filters'
	verbose_name = 'Filters'

	def ready(self):
		pass
