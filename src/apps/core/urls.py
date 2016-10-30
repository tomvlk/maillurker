from django.conf.urls import url

from . import views


urlpatterns = [
	url(r'^preference$', views.PreferenceView.as_view(), name='preference')
]
