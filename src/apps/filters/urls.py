from django.conf.urls import url

from . import views


urlpatterns = [
	url(r'^$', views.ListView.as_view(), name='list'),

	url(r'^add$', views.EditView.as_view(), name='new'),
	url(r'^edit/(?P<filterset_id>\d+)/$', views.EditView.as_view(), name='edit'),
	url(r'^delete/(?P<filterset_id>\d+)/$', views.DeleteView.as_view(), name='delete'),
]
