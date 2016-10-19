from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
	url(r'^$', views.MailList.as_view(), name='list'),
	url(r'^source/(?P<id>[0-9]+)$', views.MailList.as_view(), name='detail'),
]
