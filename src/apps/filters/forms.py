from django import forms

from apps.filters.fields import JSONFormField
from apps.filters.models import FilterSet, Rule


class AdminFilterSetEditForm(forms.ModelForm):
	pass


class AdvancedFilterSetForm(forms.Form):
	filter_name = forms.CharField(max_length=255, min_length=1, required=True)
	filter_condition = forms.ChoiceField(choices=FilterSet.COMBINE_CHOICES, widget=forms.RadioSelect,
										 required=True, initial='and')
	filter_is_global = forms.BooleanField(widget=forms.CheckboxInput, initial=False, required=False)
	filter_is_active = forms.BooleanField(widget=forms.CheckboxInput, initial=False, required=False)
	filter_icon = forms.ChoiceField(choices=FilterSet.ICON_CHOICES, initial='fa fa-filter', required=True)

	rules = JSONFormField(valid_json=True, required=True)

	def get_rules(self):
		if 'rules' not in self.cleaned_data:
			return None
		if type(self.cleaned_data['rules']) is not list:
			return None

		for raw in self.cleaned_data['rules']:
			if '_pk' in raw \
					and '_state' in raw \
					and 'negate' in raw and type(raw['negate']) is bool \
					and 'field' in raw and any(raw['field'] in key for key in Rule.FIELD_CHOICES) \
					and 'operator' in raw and any(raw['operator'] in key for key in Rule.OPERATOR_CHOICES) \
					and 'value' in raw:
				yield raw

	def update(self, instance: FilterSet):
		instance.name = self.cleaned_data['filter_name']
		instance.combine = self.cleaned_data['filter_condition']
		instance.is_global = self.cleaned_data['filter_is_global']
		instance.is_active = self.cleaned_data['filter_is_active']
		instance.icon = self.cleaned_data['filter_icon']
		return instance


class FilterSetDeleteForm(forms.Form):
	def __init__(self, *args, **kwargs):
		super(FilterSetDeleteForm, self).__init__(*args, **kwargs)
