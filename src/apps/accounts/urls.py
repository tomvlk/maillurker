from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from . import views


urlpatterns = [
	url(r'^login/$', views.Login.as_view(), name='login'),
	url(r'^logout/$', views.Logout.as_view(), name='logout'),
]
