from django.contrib import admin
from django.forms import TextInput
from django.db import models

from . import models
from . import forms


class FilterSetAdmin(admin.ModelAdmin):
	name = 'filter'
	icon = '<i class="material-icons">filter</i>'

	list_display = ('name', 'created_by', 'global_filter', 'is_active', 'icon', 'created_at', 'updated_at')
	search_fields = ('name', 'created_by', 'icon')
	list_filter = ('created_by', 'global_filter', 'is_active', 'icon')
	ordering = ('-created_at',)

	form = forms.FilterSetEditForm

	readonly_fields = ['created_at', 'updated_at']

	fieldsets = (
		(None, {
			'fields': ('name', 'icon', 'created_by', 'global_filter', 'is_active')
		}),
	)

	#add_fieldsets = (
	#	(None, {
	#		'classes': ('wide',),
	#		'fields': ('username', 'password1', 'password2')}
	#	 ),
	#)


admin.site.register(models.FilterSet, FilterSetAdmin)
