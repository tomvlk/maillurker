from django.contrib import messages
from django.shortcuts import render
from social_core.exceptions import AuthCanceled, AuthForbidden


class SocialAuthExceptionMiddleware:

	def __init__(self, get_response):
		self.get_response = get_response

	def __call__(self, request):
		response = self.get_response(request)
		return response

	def process_exception(self, request, exception):
		if type(exception) == AuthCanceled:
			messages.warning(request, 'Login session is canceled!')
			return render(request, "accounts/login.html", {})
		elif type(exception) == AuthForbidden:
			messages.error(request, 'You dont have access with this email!')
			return render(request, "accounts/login.html", {})
