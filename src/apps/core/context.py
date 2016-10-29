from apps.core.menu import Menu


def add_global_context(request):
	return {
		'navbar_menu': Menu.root,
		'user': {
			'is_authenticated': request.user.is_authenticated(),
			'is_superuser': getattr(request.user, 'is_superuser', False),
		},
		'preferences': {
			'fluid': request.session.get('preference.fluid', True)
		}
	}
