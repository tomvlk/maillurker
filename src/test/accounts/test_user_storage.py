from apps.accounts.models import User
from ..base import TestCase


class AccountsModelsTestCase(TestCase):
	fixtures = ['accounts/test_simple.json']

	def test_account_creation(self):
		user = User.objects.create(
			username='test_account',
			email='test@example.com',
		)

		self.assertIsInstance(user, User)
		self.assertIsInstance(User.objects.filter(
			username='test'
		)[0], User)

		user.delete()

		self.assertIsNone(user.pk)
