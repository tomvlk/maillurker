from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.MailList.as_view(), name='list'),
	url(r'^(?P<filter_id>[0-9]+)/$', views.MailList.as_view(), name='list-filtered'),
	url(r'^search/$', views.MailList.as_view(), name='list-search'),
]
