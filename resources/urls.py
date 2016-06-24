from django.conf.urls import patterns, url

from . import views


urlpatterns = [
    url(r'^create-resource/(?P<project_id>[-\w]+)/$', views.create_resource, name='create_resource'),
    url(r'^get_resource_properties/$', views.get_resource_properties, name='get_resource_properties'),

]
