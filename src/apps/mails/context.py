from apps.core.menu import Menu
from apps.mails.models import Message


def add_global_context(request):
	return {
		'mails': {
			'total': Message.count_all()
		}
	}
