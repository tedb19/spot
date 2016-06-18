from django.conf.urls import patterns, url

from . import views


urlpatterns = [
    url(r'^projects-listing/$', views.projects_listing, name='projects_listing'),
    url(r'^project-registration/$', views.project_registration, name='project_registration'),
]
