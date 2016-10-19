from django.contrib import admin
from django.forms import TextInput
from django.db import models

from . import models
from . import forms


class MessageAdmin(admin.ModelAdmin):
	name = 'email'
	icon = '<i class="material-icons">email</i>'

	list_display = ('peer', 'sender_name', 'sender_address', 'subject', 'size', 'type', 'created_at', 'updated_at')
	search_fields = (
		'peer', 'sender_name', 'sender_address', 'subject', 'recipients_to', 'recipients_cc',
		'recipients_bcc'
	)
	list_filter = ('type', 'peer')
	ordering = ('-created_at',)

	form = forms.MessageEditForm

	readonly_fields = ['created_at', 'updated_at']

	fieldsets = (
		('Peer', {
			'fields': ('peer', 'port')
		}),
		('Sender info', {
			'fields': ('sender_name', 'sender_address')
		}),
		('Recipients info', {
			'fields': ('recipients_to', 'recipients_cc', 'recipients_bcc')
		}),
		('Message', {
			'fields': ('subject', 'size', 'source', 'type', 'headers')
		}),
	)

	#add_fieldsets = (
	#	(None, {
	#		'classes': ('wide',),
	#		'fields': ('username', 'password1', 'password2')}
	#	 ),
	#)


admin.site.register(models.Message, MessageAdmin)
