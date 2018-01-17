from django.conf.urls import include, url
from django.contrib import admin
from .views import LoginAPIView, RegistrationAPIView, UserRetrieveUpdateAPIView

urlpatterns =  [
    url(r'^admin/', admin.site.urls),
    url(r'^user/?$', UserRetrieveUpdateAPIView.as_view()),
    url(r'^users/?$', RegistrationAPIView.as_view()),
    url(r'^users/login/?$', LoginAPIView.as_view()),
]
