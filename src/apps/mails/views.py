from django.views.generic import TemplateView

from apps.filters.models import FilterSet
from apps.mails.models import Message


class MailList(TemplateView):
	template_name = 'mails/list.html'
	sortable_columns = {
		'from': 'sender_address',
		'to': 'recipients_to',
		'subject': 'subject',
		'size': 'size',
		'received': 'created_at',
	}

	def get_context_data(self, **kwargs):
		# Sort & Order
		sort = self.request.GET.get('sort', 'received')
		order = self.request.GET.get('order', 'desc')

		if not self.sortable_columns.get(sort, None):
			sort = 'received'
			order = 'desc'

		if not order == 'asc' and not order == 'desc':
			order = 'asc'

		sort_field = self.sortable_columns.get(sort)
		print(sort_field)

		filterset = None
		if 'filter_id' in kwargs:
			try:
				filterset = FilterSet.objects.get(pk=kwargs['filter_id'])
			except:
				pass

			# Check if user has rights to access the filter set.
			if filterset and not filterset.is_global:
				if not self.request.user.is_authenticated() or not getattr(self.request.user, 'is_superuser', False)\
					or not filterset.created_by_id != self.request.user.pk:
					filterset = None

		if not filterset:
			mails = Message.objects.all()
		else:
			mails = filterset.get_matches()

		# Apply order.
		mails = mails.order_by('{}{}'.format('-' if order == 'desc' else '', sort_field))

		return {
			'list': mails,
			'sort': sort,
			'order': order,
		}
