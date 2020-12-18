from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.urls import path
from django.views.generic import TemplateView

from curry.apps.frontend import views

app_name = 'frontend'

urlpatterns = [
    url(r'^frontend/$', login_required(TemplateView.as_view(template_name='frontend/index.html'))),
    path('', views.index, name='index'),
]
