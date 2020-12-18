# curriculum/frontend/views.py
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from django.views.decorators.csrf import csrf_protect
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required


@login_required(login_url='register/', redirect_field_name='')
def index(request):
    return render(request, 'frontend/index.html')


