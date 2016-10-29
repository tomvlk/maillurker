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
def active_filter(request, filter_id):
	import re
	if re.compile(r'^/mails/{}/$'.format(filter_id)).match(request.path):
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


@register.filter
def format_addresses(value):
	if type(value) is not list:
		return ''

	addresses = []
	for entry in value:
		address = ''
		if not type(entry) is list:
			continue
		if entry[0]:
			address = '{} '.format(entry[0])
		address += ' ({})'.format(entry[1])
		addresses.append(address)

	return ', '.join(addresses)


@register.filter
def cut_small(value):
	if len(str(value)) > 40:
		return str(value)[0:37] + '...'
	return str(value)
