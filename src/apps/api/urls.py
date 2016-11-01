from django.conf.urls import url

from . import views


urlpatterns = [
	url(r'^realtime$', views.RealTimeInfos.as_view(), name='realtime'),
	url(r'^parts/(?P<part_id>[0-9]+)/$', views.PartsDetail.as_view(), name='parts_detail'),
	url(r'^mails/(?P<mail_id>[0-9]+)/$', views.MailsDetail.as_view(), name='mails_detail'),
	url(r'^mails/(?P<action>.+)/$', views.MailsAction.as_view(), name='mails_action'),
]
