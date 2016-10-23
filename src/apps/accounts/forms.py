from django import forms


class LoginForm(forms.Form):
	"""
	Login Form
	"""
	username = forms.CharField(widget=forms.TextInput)
	password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		fields = ['username', 'password']

