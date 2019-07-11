from django.contrib.admin import forms
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin


class Index(SuccessMessageMixin, LoginView):
    template_name = 'login/login.html'

    form_class = forms.AuthenticationForm
