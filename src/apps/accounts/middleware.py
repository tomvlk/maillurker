from re import compile

from django.contrib import messages
from django.shortcuts import render
from social.exceptions import AuthCanceled, AuthForbidden
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.conf import settings


EXEMPT_URLS = [
	compile(reverse(settings.LOGIN_URL).lstrip('/')),
	compile(reverse('admin:login').lstrip('/'))
]
if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
	EXEMPT_URLS += [compile(expr) for expr in settings.LOGIN_EXEMPT_URLS]


class LoginRequiredMiddleware:
	"""
	Middleware that requires a user to be authenticated to view any page other
	than LOGIN_URL. Exemptions to this requirement can optionally be specified
	in settings via a list of regular expressions in LOGIN_EXEMPT_URLS (which
	you can copy from your urls.py).

	Requires authentication middleware and template context processors to be
	loaded. You'll get an error if they aren't.
	"""
	def process_request(self, request):
		assert hasattr(request, 'user')
		if not request.user.is_authenticated():
			path = request.path_info.lstrip('/')
			if not any(m.match(path) for m in EXEMPT_URLS):
				return HttpResponseRedirect(self._login_url(path))

	def _login_url(self, path):
		admin_login_url = reverse('admin:login')
		admin_root_url = admin_login_url.split('/')[1]

		if compile('^{}.*'.format(admin_root_url)).match(path):
			return admin_login_url
		return reverse(settings.LOGIN_URL)


class SocialAuthExceptionMiddleware:
	def process_exception(self, request, exception):
		if type(exception) == AuthCanceled:
			messages.warning(request, 'Login session is canceled!')
			return render(request, "accounts/login.html", {})
		elif type(exception) == AuthForbidden:
			messages.error(request, 'You dont have access with this email!')
			return render(request, "accounts/login.html", {})
