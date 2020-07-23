from django.urls import include
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'oauth2/', include('social_django.urls', namespace='social')),
    url(r'', views.home, name='home'),
]
