from django.conf.urls import patterns, include, url
from rest_framework import viewsets, routers
from django.views.generic import TemplateView
import django_nav

#from django.contrib import admin
from django.contrib.gis import admin
admin.autodiscover()
django_nav.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'archiver.views.cover'),
    url(r'^dashboard/$', 'archiver.views.dashboard'),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
)

try:
    from local_settings import ENABLED_APIS
    for api in ENABLED_APIS:
        urlpatterns = urlpatterns + patterns('',
            url(r'^'+api+'/', include(api+'.urls')),
        )
except ImportError:
    pass
