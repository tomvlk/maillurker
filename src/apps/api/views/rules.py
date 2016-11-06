from django.db.models import Q
from django.conf import settings
from rest_framework import generics
from rest_framework import permissions
from rest_framework.exceptions import NotAuthenticated

from apps.api.permissions import UserOrAdminOrReadOnly, OwnerOrAdminOrReadOnly
from apps.filters.models import Rule
from .. import serializers


class RulesListCreate(generics.ListCreateAPIView):
	permission_classes = [UserOrAdminOrReadOnly]

	serializer_class = serializers.RuleAdvancedSerializer

	def get_queryset(self):
		if self.request.user.is_authenticated() and self.request.user.is_superuser:
			return Rule.objects.all()
		elif self.request.user.is_authenticated():
			return Rule.objects.filter(created_by=self.request.user)
		elif not settings.AUTH['allow_readonly']:
			raise NotAuthenticated()

		return Rule.objects.filter(filter_set__is_global=True)


class RulesDetail(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = [OwnerOrAdminOrReadOnly]

	serializer_class = serializers.RuleAdvancedSerializer

	lookup_field = 'pk'
	lookup_url_kwarg = 'identifier'

	def get_queryset(self):
		if self.request.user.is_authenticated() and self.request.user.is_superuser:
			return Rule.objects.all()
		elif self.request.user.is_authenticated():
			return Rule.objects.filter(created_by=self.request.user)
		elif not settings.AUTH['allow_readonly']:
			raise NotAuthenticated()

		return Rule.objects.filter(filter_set__is_global=True)
