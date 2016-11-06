from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS


class OwnerOrAdminOrReadOnly(permissions.BasePermission):

	def has_permission(self, request, view):
		return (
			request.method in SAFE_METHODS or
			(request.user and request.user.is_authenticated()) or
			(request.user and request.user.is_superuser)
		)

	def has_object_permission(self, request, view, obj):
		return (
			request.method in SAFE_METHODS or
			not obj.created_by or (
				request.user and obj.created_by == request.user
			) or (
				request.user and request.user.is_superuser
			)
		)


class UserOrAdminOrReadOnly(permissions.BasePermission):

	def has_permission(self, request, view):
		return (
			request.method in SAFE_METHODS or
			(request.user and request.user.is_authenticated()) or
			(request.user and request.user.is_superuser)
		)

	def has_object_permission(self, request, view, obj):
		return (
			request.method in SAFE_METHODS or (
				request.user and request.user.is_superuser
			)
		)
