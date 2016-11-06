from django.contrib import messages
from django.shortcuts import render
from social.exceptions import AuthCanceled, AuthForbidden


class SocialAuthExceptionMiddleware:
	def process_exception(self, request, exception):
		if type(exception) == AuthCanceled:
			messages.warning(request, 'Login session is canceled!')
			return render(request, "accounts/login.html", {})
		elif type(exception) == AuthForbidden:
			messages.error(request, 'You dont have access with this email!')
			return render(request, "accounts/login.html", {})
