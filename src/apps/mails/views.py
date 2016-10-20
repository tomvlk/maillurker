from django.views.generic import TemplateView
from django.shortcuts import render

from apps.mails.models import Message


class MailList(TemplateView):
	template_name = 'mails/list.html'

	def get(self, request, *args, **kwargs):

		queryset = Message.objects.all()

		table = {
			'header': [
				{
					'name': 'peer',
					'label': 'Peer',
					'sort': True
				}
			]
		}

		return render(request, self.template_name, {
			'table': table
		})
