from django.conf.urls import url

from . import views


urlpatterns = [
	# Front-end used calls. Not supposed for automation, can be breaking!
	url(r'^realtime$', views.website.RealTimeInfos.as_view(), name='realtime'),
	url(r'^parts/(?P<part_id>[0-9]+)/$', views.website.PartsDetail.as_view(), name='parts_detail'),
	url(r'^mails/(?P<mail_id>[0-9]+)/$', views.website.MailsDetail.as_view(), name='mails_detail'),
	url(r'^mails/(?P<action>.+)/$', views.website.MailsAction.as_view(), name='mails_action'),

	# Public API calls.
	url(r'^v1/filters/$', views.filters.FiltersListCreate.as_view(), name='filters_list'),
	url(r'^v1/filters/(?P<identifier>[0-9]+)/$', views.filters.FiltersDetails.as_view(), name='filters_single'),

	url(r'^v1/rules/$', views.rules.RulesListCreate.as_view(), name='rules_list'),
	url(r'^v1/rules/(?P<identifier>[0-9]+)/$', views.rules.RulesDetail.as_view(), name='rules_single'),
]
