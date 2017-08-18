from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
    url(r'^happy/$', views.happy, name='happy'),
    url(r'^games/$', views.games, name='games'),
    url(r'^visuals/$', views.visuals, name='visuals'),
    url(r'^animals/$', views.animals, name='animals'),
    url(r'^affirmations/$', views.affirmations, name='affirmations'),
    url(r'^spaces/$', views.spaces, name='spaces'),
    url(r'^calm/$', views.calm, name='calm'),
    url(r'^audio/$', views.audio, name='audio'),
    url(r'^c_visuals/$', views.c_visuals, name='c_visuals'),
    url(r'^meditate/$', views.meditate, name='meditate'),
    url(r'^vent/$', views.vent, name='vent'),
    url(r'^hobbies/$', views.hobbies, name='hobbies'),
    url(r'^help/$', views.help, name='help'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact_us/$', views.contact_us, name='contact_us'),
    url(r'^contact_us/twitter.com/sproutgwc/$', views.redirect_to_twitter, name='redirect_to_twitter')
    url(r'^resource/(?P<pk>\d+)/$', views.resource_detail, name='resource_detail'),
    url(r'^resource/new/$', views.resource_new, name='resource_new'),
    url(r'^resource/(?P<pk>\d+)/edit/$', views.resource_edit, name='resource_edit'),
]
