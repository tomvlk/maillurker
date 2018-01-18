from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.core.urlresolvers import reverse
from django.shortcuts import redirect

from stronghold.decorators import public


@public
def redirect_mails(request):
	return redirect(reverse('mails:list'), permanent=False)


urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
	url('', include('social_django.urls', namespace='social')),

	url(r'^$', redirect_mails, name='home'),

	url(r'^docs/', include('docs.urls')),

	url(r'^core/',		include('apps.core.urls', 		namespace='core')),
	url(r'^accounts/', 	include('apps.accounts.urls', 	namespace='accounts')),
	url(r'^mails/', 	include('apps.mails.urls', 		namespace='mails')),
	url(r'^filters/', 	include('apps.filters.urls', 	namespace='filters')),
	url(r'^api/', 		include('apps.api.urls', 		namespace='api')),
]

# Make sure media and static files work on DEV server.
if settings.DEBUG:
	import debug_toolbar

	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
	urlpatterns += [
		url(r'^__debug__/', include(debug_toolbar.urls))
	]
