from django.conf.urls import patterns, url

from . import views


urlpatterns = [
    url(r'^projects-listing/$', views.projects_listing, name='projects_listing'),
    url(r'^project-registration/$', views.project_registration, name='project_registration'),
    url(r'^project-profile/(?P<project_id>[-\w]+)/$', views.project_profile, name='project_profile'),

]
