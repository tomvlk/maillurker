from apps.accounts.models import User
from ..base import TestCase

from apps.core.smtpd import Lurker
from apps.filters import models


class FilterModelsTestCase(TestCase):
	fixtures = ['accounts/test_simple.json', 'mails/test_simple.json']

	def test_simple_filtering(self):
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

		# Should be the whole fixture sample database (50 rows).
		self.assertEqual(filterset.get_matches().count(), 50)

		# Negate rule
		rule.negate = True
		rule.save()
		self.assertEqual(filterset.get_matches().count(), 0)

		# Add rule (OR combine) for SIZE = 892.
		# Should be 8 matches
		filterset.combine = 'or'
		filterset.save()
		rule2 = models.Rule.objects.create(
			filter_set=filterset,
			field='size',
			operator='iexact',
			value='{}'.format(892),
			negate=False
		)
		self.assertIsInstance(rule2, models.Rule)
		self.assertEqual(filterset.get_matches().count(), 8)

		# Negate and check again.
		rule2.negate = True
		rule2.save()
		self.assertEqual(filterset.get_matches().count(), 42)

		# Set combine to AND and check if its 0
		filterset.combine = 'and'
		filterset.save()

		self.assertEqual(filterset.get_matches().count(), 0)

		# Delete rules and sets
		rule.delete()
		rule2.delete()
		filterset.delete()

		self.assertIsNone(filterset.pk)
		self.assertIsNone(rule.pk)
