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

		rule = models.Rule.objects.create(
			filter_set=filterset,
			field='peer',
			operator='iexact',
			value='127.0.0.1',
			negate=False
		)
		self.assertIsInstance(rule, models.Rule)

		filterset.delete()
		rule.delete()

		self.assertIsNone(filterset.pk)
		self.assertIsNone(rule.pk)
