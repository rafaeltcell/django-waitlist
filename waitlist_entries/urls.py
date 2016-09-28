from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create/$', views.create, name='create'),
    url(r'^send_me_elsewhere/$', views.send_me_elsewhere, name='send_me_elsewhere'),
]
