import json

from django import forms
from django.core.exceptions import ValidationError


class JSONFormField(forms.CharField):

	def __init__(self, valid_json=True, *args, **kwargs):
		self.valid_json = valid_json
		super(JSONFormField, self).__init__(*args, **kwargs)

	def validate(self, value):
		super(JSONFormField, self).validate(value)

		if type(value) is list or type(value) is dict:
			return value

		raise ValidationError('Invalid JSON', code='valid_json')

	def to_python(self, value):
		try:
			return json.loads(value)
		except:
			return None
