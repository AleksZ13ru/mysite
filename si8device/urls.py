from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.si8_list, name='si8_list'),
    # url(r'^chartjs/$', views.si8_, name='si8_list'),
    # Line chart
    url(r'^line_chart/$', views.line_chart, name='line_chart'),
    url(r'^line_chart/json/$', views.line_chart_json, name='line_chart_json'),
    # url(r'^line_highchart/json/$', views.line_highchart_json, name='line_highchart_json'),


    # url(r'^calendar/$', views.dept_calendar, name='dept_calendar'),
    # url(r'^calendar/(?P<year>[0-9]+)/(?P<month>[0-9]+)/$', views.dept_calendar, name='dept_calendar')
    # url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    # url(r'^post/new/$', views.post_new, name='post_new'),
    # url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
]
