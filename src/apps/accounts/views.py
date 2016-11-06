from django.conf import settings
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.shortcuts import redirect, render_to_response
from django.template import RequestContext
from django.views.generic import TemplateView, View
from rest_framework.authtoken.models import Token
from social.apps.django_app.utils import get_backend, BACKENDS
from stronghold.views import StrongholdPublicMixin

from apps.accounts.utils import get_social_button
from apps.core.utils import fullname
from . import forms


class Login(StrongholdPublicMixin, TemplateView):
	template_name = 'accounts/login.html'

	@property
	def social_config(self):
		buttons = list()

		for backend in settings.SOCIAL_BACKENDS:
			buttons.append(get_social_button(backend))

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


class Details(TemplateView):
	template_name = 'accounts/details.html'

	def get_context_data(self, **kwargs):

		token = None
		if settings.USER_API_KEYS:
			token, _ = Token.objects.get_or_create(user=self.request.user)

		social_accounts = self.request.user.social_auth.all()

		accounts = list()

		for social_account in social_accounts:
			backend = get_backend(BACKENDS, social_account.provider)
			infos = None
			try:
				infos = get_social_button(fullname(backend))
			except Exception as e:
				pass

			accounts.append({
				'provider': social_account.provider,
				'id': social_account.id,
				'backend': backend,
				'infos': infos
			})

		return {
			'user': self.request.user,
			'token': token,
			'social_accounts': accounts,
			'avatar': self.request.user.get_gravatar_url(size=80, default='mm')
		}
