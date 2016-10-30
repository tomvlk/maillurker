from django.db import models as db_models

from apps.accounts.models import User
from ..base import TestCase

from apps.core.smtpd import Lurker
from apps.filters import models


class FilterModelsTestCase(TestCase):
	fixtures = ['accounts/test_simple.json']

	def test_filter_creation(self):
		filterset = models.FilterSet.objects.create(
			name='Test Filter',
			created_by=User.objects.get(pk=1),
			is_global=True,
			is_active=True,
			icon='fa fa-filter',
			combine='and'
		)
		self.assertIsInstance(filterset, models.FilterSet)

		self.assertEqual(filterset.name, 'Test Filter')
		self.assertEqual(filterset.created_by_id, 1)
		self.assertEqual(filterset.created_by.pk, 1)
		self.assertEqual(filterset.is_global, True)
		self.assertEqual(filterset.is_active, True)
		self.assertEqual(filterset.icon, 'fa fa-filter')
		self.assertEqual(filterset.combine, 'and')

		rule = models.Rule.objects.create(
			filter_set=filterset,
			field='peer',
			operator='iexact',
			value='127.0.0.1',
			negate=False
		)
		self.assertIsInstance(rule, models.Rule)

		self.assertEqual(rule.filter_set, filterset)
		self.assertEqual(rule.field, 'peer')
		self.assertEqual(rule.operator, 'iexact')
		self.assertEqual(rule.value, '127.0.0.1')
		self.assertEqual(rule.negate, False)

		filterset.delete()
		rule.delete()

		self.assertIsNone(filterset.pk)
		self.assertIsNone(rule.pk)

	def test_filter_meta(self):
		self.assertEqual(models.FilterSet.get_combine_choices(), dict(models.FilterSet.COMBINE_CHOICES))
		self.assertEqual(models.FilterSet.get_icon_choices(), dict(models.FilterSet.ICON_CHOICES))
