from crispy_forms.bootstrap import StrictButton
from django import forms
from django.core.urlresolvers import reverse
from django.forms.util import ErrorList
from django.utils import timezone
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Field

from apps.filters.models import FilterSet


class AdminFilterSetEditForm(forms.ModelForm):
	pass


class FilterSetForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(FilterSetForm, self).__init__(*args, **kwargs)

		self.helper = FormHelper()
		self.helper.form_id = 'filterset-form'
		self.helper.form_method = 'post'
		if 'data' in kwargs and kwargs['data']:
			self.helper.form_action = reverse('filters:edit')
		else:
			self.helper.form_action = reverse('filters:new')

		self.helper.form_class = 'form-horizontal'
		self.helper.label_class = 'col-lg-2'
		self.helper.field_class = 'col-lg-8'
		self.helper.layout = Layout(
			'name',
			'icon',
			StrictButton('Submit', css_class='btn-default', type='submit'),
		)

	class Meta:
		model = FilterSet
		fields = ('name', 'icon')
