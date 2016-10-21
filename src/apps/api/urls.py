from django.conf.urls import url

from . import views


urlpatterns = [
	url(r'^realtime$', views.RealTimeInfos.as_view(), name='realtime'),
]
