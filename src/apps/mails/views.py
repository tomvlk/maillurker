from django.views.generic import TemplateView
from django.shortcuts import render

from apps.filters.models import FilterSet
from apps.mails.models import Message


class MailList(TemplateView):
	template_name = 'mails/list.html'

	def get_context_data(self, **kwargs):
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

		return {'list': mails}
