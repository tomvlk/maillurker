from django.views.generic import TemplateView
from django.shortcuts import render


class MailList(TemplateView):
	template_name = 'mails/list.html'

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name, {})
