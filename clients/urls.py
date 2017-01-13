from django.conf.urls import url

from . import views

app_name = 'clients'

urlpatterns = [
    url(r'^$', views.ClientList.as_view(), name='list'),
    url(r'^(?P<pk>[0-9]+)/$', views.ClientDetail.as_view(), name='detail'),
    url(r'^create/$', views.ClientCreate.as_view(), name='create'),
    url(r'^(?P<pk>[0-9]+)/update/$', views.ClientUpdate.as_view(), name='update'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.ClientDelete.as_view(), name='delete'),
]
