import locale

from django import template

register = template.Library()


@register.filter
def currency(value):
	try:
		return locale.currency(value, grouping=True)
	except Exception:
		return locale.currency(0.0, grouping=True)


@register.simple_tag
def active(request, pattern):
	import re
	if re.compile(pattern).match(request.path):
		return 'active'
	return ''


@register.simple_tag
def collapse(request, pattern):
	import re
	if re.compile(pattern).match(request.path):
		return 'in'
	return ''


@register.assignment_tag
def get_bootstrap_alert_msg_css_name(tags):
	return 'danger' if tags == 'error' else tags
