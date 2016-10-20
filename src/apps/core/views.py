from django.shortcuts import redirect
from django.views.generic import View


class SearchView(View):

	def get(self, request, *args, **kwargs):
		# TODO: Implement search
		return redirect('/')
