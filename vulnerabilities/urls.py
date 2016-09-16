from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^search/', views.search, name='search'),
    url(r'^sql_exception/', views.sql_exception, name='SQL Exception'),
    url(r'^(?P<project_id>.*)/$', views.project_show, name='project_show'),
]


