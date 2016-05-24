from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^sql_exception/', views.sql_exception, name='SQL Exception'),
]
