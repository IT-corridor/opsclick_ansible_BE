from django.conf.urls import include, url

from . import views

service_patterns = ([
    url(r'^$', views.service_list, name='service_list'),
    url(r'^(?P<service_name>[\w-]+)$', views.service_detail, name='service_detail')
], 'service')

setup_patterns = ([
    url(r'^$', views.setup_service, name='setup_service'),
], 'setup')

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^service', include(service_patterns)),
    url(r'^setup', include(setup_patterns)),
]
