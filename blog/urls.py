from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.resource_list, name='resource_list'),
]
