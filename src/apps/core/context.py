from apps.core.menu import Menu


def add_global_context(request):
	return {
		'navbar_menu': Menu.root,
		'user': {
			'is_authenticated': request.user.is_authenticated(),
			'is_superuser': getattr(request.user, 'is_superuser', False),
		},

		'total_mails': 51,
		'filters': {
			'servers': [
				{
					'id': 1,
					'alias': 'DEV01',
					'ip': '1.1.1.1',
					'mails': 12
				},
				{
					'id': 2,
					'alias': 'DEV02',
					'ip': '2.2.2.2',
					'mails': 24
				},
				{
					'id': 3,
					'alias': 'DEV03',
					'ip': '3.3.3.3',
					'mails': 9
				},
			]
		}
	}
