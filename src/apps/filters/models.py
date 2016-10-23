from django.conf import settings
from django.db import models
from django.db.models import Q
from jsonfield import JSONField

from apps.accounts.models import User
from apps.core.models import BaseModel


class FilterSet(BaseModel):
	ICON_CHOICES = (
		('fa fa-filter', 'Default Filter'),
		('fa fa-server', 'Server'),
	)

	COMBINE_CHOICES = (
		('and', 'Match all criteria (AND)'),
		('or', 'Match one of the criteria (OR)')
	)

	name = models.CharField(max_length=255)
	"""Name of the filter"""

	created_by = models.ForeignKey(User, related_name='created_filters')
	"""Couple filter to user. Use this especially when filter is not global but user defined."""

	is_global = models.BooleanField(default=False)
	"""Set true if the filter is global"""

	is_active = models.BooleanField()
	"""Filter active. True to show in the filter list."""

	icon = models.CharField(max_length=255, choices=ICON_CHOICES, default='fa fa-filter')
	"""Icon to show in the list."""

	combine = models.CharField(max_length=3, choices=COMBINE_CHOICES, default='and')
	"""Combine of the rules"""


	@staticmethod
	def get_icon_choices():
		return dict(FilterSet.ICON_CHOICES)

	@staticmethod
	def get_combine_choices():
		return dict(FilterSet.COMBINE_CHOICES)

	def get_matches(self):
		# TODO, decode criteria and match against messages.
		# TODO, use cache
		return Rule.objects.all()

	@property
	def count(self):
		if getattr(self, '_count', None) is None:
			self._count = self.get_matches().count()
		return self._count


class Rule(BaseModel):
	OPERATOR_CHOICES = (
		('iexact', 'Equal Than (==)'),
		('icontains', 'Contains'),
		('iregex', 'Matches Regular Expression'),
		('isnull', 'Is NULL'),
		('istrue', 'Is TRUE'),
		('isfalse', 'Is FALSE'),
		('lt', 'Less Than (<)'),
		('gt', 'Greater Than (>)'),
		('lte', 'Less or Equal Than (<=)'),
		('gte', 'Greater or Equal Than (>=)'),
	)

	FIELD_CHOICES = (
		('peer', 'Peer Address'),
		('port', 'Peer Port'),
		('sender_name', 'Sender Name'),
		('sender_address', 'Sender Address'),
		('recipients_to', 'To Recipients'),
		('recipients_cc', 'CC Recipients'),
		('recipients_bcc', 'BCC Recipients'),
		('subject', 'Subject'),
		('size', 'Message Size'),
		('type', 'Message Content Type'),
		('headers', 'Message Headers'),
	)

	filter_set = models.ForeignKey(FilterSet, related_name='rules')

	field = models.CharField(max_length=255, choices=FIELD_CHOICES)
	"""Field to run condition against."""

	operator = models.CharField(max_length=255, choices=OPERATOR_CHOICES)
	"""Operator"""

	negate = models.BooleanField(default=False)
	"""Negate condition"""

	value = JSONField()

	pass
