from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from . import views


urlpatterns = [
	url(r'^$', views.ListView.as_view(), name='list'),

	url(r'^add$', views.EditView.as_view(), name='new'),
	url(r'^edit/<P(filterset_id)[0-9]>$', views.EditView.as_view(), name='edit'),
]
