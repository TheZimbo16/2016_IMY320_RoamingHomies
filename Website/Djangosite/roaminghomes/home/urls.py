from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^about/$', views.about, name='about'),
	url(r'^contact/$', views.contact, name='contact'),
	url(r'^events/$', views.list, name='event_list'),
	url(r'^calendar/$', views.calendar, name='calendar'),
]