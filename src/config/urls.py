from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from django.views.generic import RedirectView


urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),

	url(r'^$', RedirectView.as_view(url='/mails/', permanent=False), name='home'),

	url(r'^core/', include('apps.core.urls', namespace='core')),
	url(r'^accounts/', include('apps.accounts.urls', namespace='accounts')),
	url(r'^mails/', include('apps.mails.urls', namespace='mails')),
	url(r'^filters/', include('apps.filters.urls', namespace='filters')),
]


# Make sure media and static files work on DEV server.
if settings.DEBUG:
	urlpatterns += [
		url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT})
	]
