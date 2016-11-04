from django.contrib import messages
from django.core.urlresolvers import reverse
from django.db import transaction
from django.shortcuts import redirect
from django.views import generic

from apps.core.mixins import LoginRequiredMixin
from apps.filters.models import FilterSet, Rule

from . import forms


class ListView(generic.TemplateView):
	template_name = 'filters/list.html'

	def get_context_data(self, **kwargs):
		return {
			'filters': FilterSet.objects.all()
		}


class EditView(LoginRequiredMixin, generic.TemplateView):
	template_name = 'filters/edit.html'

	def get(self, request, *args, **kwargs):
		filterset = FilterSet()

		if 'filterset_id' in kwargs:
			try:
				filterset = FilterSet.objects.get(pk=kwargs['filterset_id'])
			except Exception:
				return redirect(reverse('filters:list'))

		rules = filterset.rules.all()

		return self.render_to_response({
			'filterset': filterset,
			'rules': rules
		})

	def post(self, request, *args, **kwargs):
		form = forms.AdvancedFilterSetForm(request.POST)
		filterset = FilterSet()

		if 'filterset_id' in kwargs:
			try:
				filterset = FilterSet.objects.get(pk=kwargs['filterset_id'])
			except:
				pass

		valid = form.is_valid()

		if not valid:
			print(form.errors)
			if filterset.pk:
				return redirect(reverse('filters:edit', kwargs={'filterset_id': filterset.pk}))
			else:
				return redirect(reverse('filters:add'))

		# Add/Update filterset itself.
		filterset = form.update(filterset)

		# Validate if user is allowed to add/edit globals
		is_superuser = getattr(request.user, 'is_superuser', False)
		if not is_superuser:
			if filterset.is_global:
				return redirect(reverse('filters:list'))

			if filterset.created_by_id is not None and filterset.created_by_id != request.user.pk:
				return redirect(reverse('filters:list'))

		# If new filterset, couple the user with it.
		if filterset.created_by_id is None:
			filterset.created_by = request.user

		# Save set.
		filterset.save()

		# Parse rules. Get existing and cleanup all others
		with transaction.atomic():
			filterset.rules.all().delete()
			for raw_rule in form.get_rules():
				Rule.objects.create(
					filter_set=filterset,
					field=raw_rule['field'],
					operator=raw_rule['operator'],
					negate=raw_rule['negate'],
					value=raw_rule['value']
				)

		messages.add_message(request, messages.SUCCESS, 'Filter has been added!')
		return redirect(reverse('filters:list'))


class DeleteView(LoginRequiredMixin, generic.TemplateView):
	template_name = 'filters/delete.html'

	def get(self, request, *args, **kwargs):
		try:
			filterset = FilterSet.objects.get(pk=kwargs['filterset_id'])
		except Exception:
			return redirect(reverse('filters:list'))

		if not getattr(request.user, 'is_superuser', False) and not request.user == filterset.created_by:
			return redirect(reverse('filters:list'))

		return self.render_to_response({'filter': filterset})

	def post(self, request, *args, **kwargs):
		try:
			filterset = FilterSet.objects.get(pk=kwargs['filterset_id'])
		except Exception:
			return redirect(reverse('filters:list'))

		if not getattr(request.user, 'is_superuser', False) and not request.user == filterset.created_by:
			return redirect(reverse('filters:list'))

		filterset.rules.all().delete()
		filterset.delete()

		return redirect(reverse('filters:list'))
