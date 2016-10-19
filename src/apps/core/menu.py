from django.core.urlresolvers import reverse


class Menu:
	root = None

	@staticmethod
	def add_item(item, path=''):
		# If no root has been defined, set a new root menu.
		if not Menu.root:
			Menu.root = Item('ROOT')

		root = Menu.root
		depth = 1
		for part in path.split('/'):
			if part:
				new_root = root.child_by_name(part)

				if not new_root:
					new_root = Item(part, label=str(part).capitalize())
					new_root.depth = depth
					root.add(new_root)

				root = new_root

			depth += 1

		item.depth = depth
		root.add(item)

	@staticmethod
	def to_string():
		# TODO: Get debug string of menu.
		pass


class Item:
	def __init__(self, name, label='', icon='', route_name='', active_regex='^$', order=0):
		self.name = name
		self.label = label
		self.icon = icon
		self.route_name = route_name
		self.active_regex = active_regex
		self.order = order

		self.depth = 1
		self.children = list()

	def add(self, item):
		"""Add entry as child to the menuitem"""
		idx = 0
		for child in self.children:
			if item.order < child.order:
				break
			idx += 1

		self.children = self.children[:idx] + [item] + self.children[idx:]

	def child_by_name(self, name):
		"""Find child by name"""
		for child in self.children:
			if child.name == name:
				return child
		return None


	@property
	def url(self):
		try:
			return reverse(self.route_name)
		except Exception:
			return '#'

	def __str__(self):
		string = self.name + ' childs:\n'
		for child in self.children:
			string += str(child) + '\t'
		return string
