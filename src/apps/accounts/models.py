import hashlib

from django.contrib.auth import models
from django.utils.http import urlencode


class User(models.AbstractUser):

	def get_gravatar_url(self, size=120, default='mm'):
		"""
		Get Gravatar URL.
		:param size:
		:param default:
		:return:
		"""

		iden = self.get_username()
		if self.email:
			iden = self.email

		encoded = hashlib.md5(iden.lower().encode('utf-8'))

		return 'https://www.gravatar.com/avatar/{}?{}'.format(
			encoded,
			urlencode({'d': default, 's': str(size)})
		)
