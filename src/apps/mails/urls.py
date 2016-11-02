from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.MailList.as_view(), name='list'),
	url(r'^(?P<filter_id>[0-9]+)/$', views.MailList.as_view(), name='list-filtered'),
	url(r'^(?P<mail_id>[0-9]+)/parts/(?P<part_id>[0-9]+)/$', views.MailPart.as_view(), name='part'),
	url(r'^(?P<mail_id>[0-9]+)/parts/(?P<part_id>[0-9]+)/body$', views.MailPartBody.as_view(), name='part-body',
		kwargs={'response_type': 'body'}),
	url(r'^(?P<mail_id>[0-9]+)/parts/(?P<part_id>[0-9]+)/source$', views.MailPartBody.as_view(), name='part-source',
		kwargs={'response_type': 'source'}),
	url(r'^(?P<mail_id>[0-9]+)/parts/(?P<part_id>[0-9]+)/download$', views.MailPartBody.as_view(), name='part-download',
		kwargs={'response_type': 'download'}),
	url(r'^download/(?P<mail_ids>[0-9,]+)/$', views.MailDownload.as_view(), name='download'),
	url(r'^search/$', views.MailList.as_view(), name='list-search'),
]
