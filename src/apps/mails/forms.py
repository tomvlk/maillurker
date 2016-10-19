from django import forms
from django.forms.util import ErrorList
from django.utils import timezone
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Field


class MessageEditForm(forms.ModelForm):
	peer = forms.GenericIPAddressField(required=True, label='Remote Peer')

	port = forms.IntegerField(required=True, label='Remote Port')

	source = forms.CharField(required=True, label='Source', widget=forms.Textarea(attrs={
		'rows': 25,
		'style': 'height: 25em;'
	}))
