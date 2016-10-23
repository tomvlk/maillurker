from django.contrib import admin

from . import models
from . import forms


class FilterSetAdmin(admin.ModelAdmin):
	name = 'filter'
	icon = '<i class="material-icons">filter</i>'

	list_display = ('name', 'created_by', 'is_global', 'is_active', 'icon', 'created_at', 'updated_at')
	search_fields = ('name', 'created_by', 'icon')
	list_filter = ('created_by', 'is_global', 'is_active', 'icon')
	ordering = ('-created_at',)

	form = forms.AdminFilterSetEditForm

	readonly_fields = ['created_at', 'updated_at']

	fieldsets = (
		(None, {
			'fields': ('name', 'icon', 'created_by', 'is_global', 'is_active')
		}),
	)

admin.site.register(models.FilterSet, FilterSetAdmin)
