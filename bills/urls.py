from django.conf.urls import url

from . import views

app_name = 'bills'

urlpatterns = [
    url(r'^create/$', views.CreateView.as_view(), name='create'),
    url(r'^$', views.ListView.as_view(), name='list'),
    url(r'^(?P<pk>[0-9]+)/update/$', views.UpdateView.as_view(), name='update'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.DeleteView.as_view(), name='delete'),
]
