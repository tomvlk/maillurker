from django.conf.urls import url

from . import views


urlpatterns = [
	url(r'^search/$', views.SearchView.as_view(), name='search'),

	url(r'^preference$', views.PreferenceView.as_view(), name='preference')
]
