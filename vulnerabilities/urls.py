from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^search/', views.search, name='search'),
    url(r'^sql_exception/', views.sql_exception, name='SQL Exception'),
    url(r'^send_me_json/$', views.send_me_json, name='send_me_json'),
]
