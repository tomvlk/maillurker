import importlib

from django.conf import settings
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.shortcuts import redirect, render_to_response
from django.template import RequestContext
from django.views.generic import TemplateView, View

from . import forms


class Login(TemplateView):
	template_name = 'accounts/login.html'

	@property
	def social_config(self):
		buttons = list()

		for backend in settings.SOCIAL_BACKENDS:
			module_name = backend[0:(str(backend).rindex('.'))]
			class_name = backend[(len(module_name) + 1):]
			module = importlib.import_module(module_name)
			clazz = getattr(module, class_name)

			buttons.append({
				'name': getattr(clazz, 'name', class_name)
			})

		return {
			'enabled': settings.SOCIAL_ENABLED,
			'backends': settings.SOCIAL_BACKENDS,
			'buttons': buttons
		}

	def get(self, request, *args, **kwargs):
		redirect_url = request.GET.get('next', '/')
		if not redirect_url:
			redirect_url = '/'

		if request.user.is_authenticated():
			return redirect(redirect_url)

		form = forms.LoginForm()

		return render_to_response(self.template_name, {
			'form': form,
			'next': redirect_url,
			'social': self.social_config
		}, context_instance=RequestContext(request))

	def post(self, request, *args, **kwargs):
		form = forms.LoginForm(data=request.POST)
		redirect_url = request.GET.get('next', '/')
		if not redirect_url:
			redirect_url = '/'

		if form.is_valid():
			user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])

			if user is not None:
				if user.is_active:
					django_login(request, user)
					return redirect(redirect_url)
			form.errors['__all__'] = form.error_class(["Email and password combination is wrong"])

		return render_to_response(self.template_name, {
			'form': form,
			'next': redirect_url,
			'social': self.social_config
		}, context_instance=RequestContext(request))


class Logout(View):

	def get(self, request, *args, **kwargs):
		django_logout(request)
		return redirect('/')
