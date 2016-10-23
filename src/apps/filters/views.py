from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views import generic

from apps.core.mixins import LoginRequiredMixin
from apps.filters.models import FilterSet

from . import forms


class ListView(generic.TemplateView):
	template_name = 'filters/list.html'

	def get_context_data(self, **kwargs):
		return {
			'filters': FilterSet.objects.all()
		}


class EditView(LoginRequiredMixin, generic.TemplateView):
	template_name = 'filters/edit.html'

	def get(self, request, *args, **kwargs):
		filterset = FilterSet()

		if 'filterset_id' in kwargs:
			try:
				filterset = FilterSet.objects.get(pk=kwargs['filterset_id'])
			except Exception:
				return redirect(reverse('filters:list'))

		rules = filterset.rules.all()

		form = forms.FilterSetForm(instance=filterset)
		return self.render_to_response({
			'form': form,
			'filterset': filterset,
			'rules': rules
		})


class DeleteView(LoginRequiredMixin, generic.TemplateView):
	template_name = 'filters/delete.html'

	def get(self, request, *args, **kwargs):
		try:
			filterset = FilterSet.objects.get(pk=kwargs['filterset_id'])
		except Exception:
			return redirect(reverse('filters:list'))

		if not getattr(request.user, 'is_superuser', False) and not request.user == filterset.created_by:
			return redirect(reverse('filters:list'))

		return self.render_to_response({'filter': filterset})

	def post(self, request, *args, **kwargs):
		try:
			filterset = FilterSet.objects.get(pk=kwargs['filterset_id'])
		except Exception:
			return redirect(reverse('filters:list'))

		if not getattr(request.user, 'is_superuser', False) and not request.user == filterset.created_by:
			return redirect(reverse('filters:list'))

		filterset.criteria.all().delete()
		filterset.delete()

		return redirect(reverse('filters:list'))
