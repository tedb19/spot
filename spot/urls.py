from django.conf.urls import url, include

urlpatterns = [
    url(r'^user/', include('user_account.urls')),
    url(r'^projects/', include('project.urls')),
]
