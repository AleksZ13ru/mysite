from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.docx_list, name='docx_list'),
    url(r'^(?P<pk>[0-9]+)/$', views.docx_detail, name='docx_detail'),
    url(r'^new/$', views.docx_new, name='docx_new'),
    url(r'^(?P<pk>[0-9]+)/event_new/$', views.event_new, name='event_new'),
    url(r'^(?P<pk>[0-9]+)/note_new/$', views.note_new, name='note_new'),
    url(r'^(?P<pk>[0-9]+)/edit/$', views.docx_edit, name='docx_edit'),
    # url(r'^calendar/$', views.dept_calendar, name='dept_calendar'),
    # url(r'^calendar/(?P<year>[0-9]+)/(?P<month>[0-9]+)/$', views.dept_calendar, name='dept_calendar')
    # url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    # url(r'^post/new/$', views.post_new, name='post_new'),
    # url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
]
