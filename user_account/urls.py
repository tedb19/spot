from django.conf.urls import patterns, url

from . import views


urlpatterns = [
    url(r'^sign-up/$', views.registration, name='registration'),
    url(r'^success/(?P<pk>[-\w]+)/$', views.success, name='success'),
    url(r'^login/$', views.LoginRequest, name='user_login'),
    url(r'^logout/$', views.LogoutRequest, name='user_logout'),
    url(r'^home/$', views.home, name='home'),
]
