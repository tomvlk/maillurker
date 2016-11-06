from django.conf import settings
from django.db.models import Q
from rest_framework import generics
from rest_framework import permissions
from rest_framework.exceptions import NotAuthenticated

from apps.api.permissions import OwnerOrAdminOrReadOnly, UserOrAdminOrReadOnly
from apps.filters.models import FilterSet
from .. import serializers


class FiltersListCreate(generics.ListCreateAPIView):
	permission_classes = [UserOrAdminOrReadOnly]

	serializer_class = serializers.FilterSetAdvancedSerializer

	def get_queryset(self):
		if self.request.user.is_authenticated():
			return FilterSet.objects.filter(Q(is_global=True) | Q(created_by=self.request.user))
		elif not settings.AUTH['allow_readonly']:
			raise NotAuthenticated()

		return FilterSet.objects.filter(is_global=True)

	def perform_create(self, serializer):
		serializer.save(created_by=self.request.user)


class FiltersDetails(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = [OwnerOrAdminOrReadOnly]

	serializer_class = serializers.FilterSetAdvancedSerializer

	lookup_field = 'pk'
	lookup_url_kwarg = 'identifier'

	def get_queryset(self):
		if self.request.user.is_authenticated():
			return FilterSet.objects.filter(Q(is_global=True) | Q(created_by=self.request.user))
		elif not settings.AUTH['allow_readonly']:
			raise NotAuthenticated()

		return FilterSet.objects.filter(is_global=True)

	def perform_create(self, serializer):
		serializer.save(created_by=self.request.user)
