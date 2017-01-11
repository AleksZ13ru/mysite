from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.parsing, name='si8_parsing'),
    url(r'^findfile$', views.si8_find_file, name='si8_find_file'),
    url(r'^parsfile/(?P<pk>[0-9]+)/$', views.si8_pars_file, name='si8_pars_file')

    # url(r'^calendar/$', views.dept_calendar, name='dept_calendar'),
    # url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    # url(r'^post/new/$', views.post_new, name='post_new'),
    # url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
]
