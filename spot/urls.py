from django.conf.urls import url, include
from user_account.views import home


urlpatterns = [
    url(r'^user/', include('user_account.urls')),
    url(r'^projects/', include('project.urls')),
    url(r'^project-resources/', include('resources.urls')),
    url(r'^$', home),
]
