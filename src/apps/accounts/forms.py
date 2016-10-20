from django import forms
from django.forms.util import ErrorList
from django.utils import timezone
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Field


class LoginForm(forms.Form):
	"""
	Login Form
	"""
	username = forms.CharField(widget=forms.TextInput)
	password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		fields = ['username', 'password']

