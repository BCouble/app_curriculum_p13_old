from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import *
from django.conf import settings
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView

from curry.apps.register.forms import CustomUserCreationForm


class LoginView(TemplateView):
    """ connection view """
    template_name = 'register/register.html'

    def post(self, request, **kwargs):
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)

        return render(request, self.template_name)


class LogoutView(TemplateView):
    """ disconnect view """
    template_name = 'register/register.html'

    def get(self, request, **kwargs):
        logout(request)

        return render(request, self.template_name)


class UserCreateView(FormView):
    template_name = 'register/register_form.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('register:register')

    def form_valid(self, form):
        form.save()

        return super().form_valid(form)
