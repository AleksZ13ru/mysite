from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.daybook_list, name='daybook_list'),
    # url(r'^all/$', views.docx_all, name='docx_all'),
    # url(r'^executor/(?P<pk>[0-9]+)/$', views.docx_executor, name='docx_executor'),
    # url(r'^destination/(?P<pk>[0-9]+)/$', views.docx_destination, name='docx_destination'),
    # url(r'^calendar/(?P<year>[0-9]+)/(?P<month>[0-9]+)/$', views.docx_calendar, name='docx_calendar'),
    # url(r'^(?P<pk>[0-9]+)/$', views.docx_detail, name='docx_detail'),
    url(r'^new/$', views.daybook_new, name='daybook_new'),
    # url(r'^(?P<pk>[0-9]+)/event_new/$', views.event_new, name='event_new'),
    # url(r'^(?P<pk>[0-9]+)/event_del/$', views.event_del, name='event_del'),
    # url(r'^(?P<pk>[0-9]+)/note_new/$', views.note_new, name='note_new'),
    # url(r'^(?P<pk>[0-9]+)/note_del/$', views.note_del, name='note_del'),
    # url(r'^(?P<pk>[0-9]+)/edit/$', views.docx_edit, name='docx_edit'),

]
