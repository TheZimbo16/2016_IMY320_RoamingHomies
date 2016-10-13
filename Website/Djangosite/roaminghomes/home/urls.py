from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^about/$', views.about, name='about'),
	url(r'^contact/$', views.contact, name='contact'),
	
	url(r'^events/$', views.list, name='event_list'),
	url(r'^events/(?P<id>\d+)/$', views.detail, name='event_detail'),
	url(r'^events/create', views.add_event, name='event_add'),
	url(r'^events/volunteer/(?P<event_id>\d+)/$', views.volunteer, name='event_attend'),
	url(r'^events/cancel/(?P<event_id>\d+)/$', views.cancel, name='event_cancel'),
	
	url(r'^calendar/$', views.calendar, name='calendar'),
	url(r'^uploads/$', views.listUploads, name='upload_list'),
	url(r'^uploads/upload$', views.uploadFile, name='upload'),	
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)