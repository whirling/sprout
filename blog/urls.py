from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.resource_list, name='resource_list'),
    url(r'^resource/(?P<pk>\d+)/$', views.resource_detail, name='resource_detail'),
    url(r'^resource/new/$', views.resource_new, name='resource_new'),
]
