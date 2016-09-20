from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^search/', views.search, name='search'),
    url(r'^sql_exception/', views.sql_exception, name='SQL Exception'),
]
