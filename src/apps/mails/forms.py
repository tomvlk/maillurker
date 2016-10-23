from django import forms


class MessageEditForm(forms.ModelForm):
	peer = forms.GenericIPAddressField(required=True, label='Remote Peer')

	port = forms.IntegerField(required=True, label='Remote Port')

	source = forms.CharField(required=True, label='Source', widget=forms.Textarea(attrs={
		'rows': 25,
		'style': 'height: 25em;'
	}))
