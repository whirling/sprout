from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
    url(r'^happy/$', views.happy, name='happy'),
    url(r'^games/$', views.games, name='games'),
    url(r'^visuals/$', views.visuals, name='visuals'),
    url(r'^calm/$', views.calm, name='calm'),
    url(r'^help/$', views.help, name='help'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact_us/$', views.contact_us, name='contact_us'),
    url(r'^resource/(?P<pk>\d+)/$', views.resource_detail, name='resource_detail'),
    url(r'^resource/new/$', views.resource_new, name='resource_new'),
    url(r'^resource/(?P<pk>\d+)/edit/$', views.resource_edit, name='resource_edit'),
]
