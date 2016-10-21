from django.apps import AppConfig

from apps.core.menu import Item
from apps.core.menu import Menu


class FiltersConfig(AppConfig):
	name = 'apps.filters'
	verbose_name = 'Filters'

	def ready(self):

		Menu.add_item(Item(
			name='filters',
			label='Filters',
			route_name='filters:list',
			active_regex='^(/filters/)',
		))
