from django.contrib import messages
from django.contrib.admin import forms as admin_forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views import generic

from login import forms


class Create(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    template_name = 'login/create.html'

    form_class = forms.FormCreate

    success_url = reverse_lazy('roster:search')

    success_message = _('Employee has been created.')


class Delete(LoginRequiredMixin, generic.DeleteView):
    success_url = reverse_lazy('roster:search')

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()

        if obj.is_superuser:
            messages.add_message(request, messages.INFO, _('Administrator cannot be removed.'))

            return redirect(self.success_url)
        else:
            messages.success(self.request, _('Employee has been removed.'))

            return super(Delete, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return get_object_or_404(get_user_model(), pk=self.kwargs['pk'], is_staff=True)


class Index(SuccessMessageMixin, LoginView):
    template_name = 'login/login.html'

    form_class = admin_forms.AuthenticationForm


class Password(LoginRequiredMixin, SuccessMessageMixin, PasswordChangeView):
    form_class = PasswordChangeForm

    template_name = 'login/password.html'

    success_url = reverse_lazy('login:password')

    success_message = _('Updated password.')
