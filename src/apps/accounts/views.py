from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.shortcuts import redirect, render_to_response
from django.template import RequestContext
from django.views.generic import TemplateView, View

from . import forms


class Login(TemplateView):
	template_name = 'accounts/login.html'

	def get(self, request, *args, **kwargs):
		redirect_url = request.GET.get('next', '/')
		if not redirect_url:
			redirect_url = '/'

		if request.user.is_authenticated():
			return redirect(redirect_url)

		form = forms.LoginForm()

		return render_to_response(self.template_name, {
			'form': form,
			'next': redirect_url
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
			'next': redirect_url
		}, context_instance=RequestContext(request))


class Logout(View):

	def get(self, request, *args, **kwargs):
		django_logout(request)
		return redirect('/')
