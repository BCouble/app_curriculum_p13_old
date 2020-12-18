from django.conf.urls import url
from django.urls import path

from curry.apps.register.views import LoginView, LogoutView, UserCreateView

app_name = 'register'

urlpatterns = [
    url(r'^$', LoginView.as_view(), name='register'),
    url(r'^$', LogoutView.as_view()),
    path('user-add/', UserCreateView.as_view(), name='register-add'),
]
