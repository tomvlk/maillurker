from django.views.generic import TemplateView

from apps.filters.models import FilterSet

from . import forms


class ListView(TemplateView):
	template_name = 'filters/list.html'

	def get_context_data(self, **kwargs):
		return {
			'filters': FilterSet.objects.all()
		}


class EditView(TemplateView):
	template_name = 'filters/edit.html'

	def get(self, request, *args, **kwargs):
		form = forms.FilterSetForm()
		return self.render_to_response({'form': form})
