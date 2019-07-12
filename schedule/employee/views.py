from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views import generic

from schedule.employee import forms
from schedule.employee import models


class Add(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    form_class = forms.FormAdd

    template_name = 'employee/add.html'

    success_url = reverse_lazy('employee:search')

    success_message = _('Created Employee Profile.')


class Delete(LoginRequiredMixin, generic.DeleteView):
    success_url = reverse_lazy('employee:search')

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()

        if obj.is_superuser:
            messages.add_message(request, messages.INFO, _('Administrator account cannot be removed.'))

            return redirect(self.success_url)
        else:
            messages.success(self.request, _('Employee account has been removed.'))

            return super(__class__, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return get_object_or_404(models.Account, pk=self.kwargs['pk'], is_staff=True)


class Password(LoginRequiredMixin, SuccessMessageMixin, PasswordChangeView):
    form_class = PasswordChangeForm

    template_name = 'employee/password.html'

    success_url = reverse_lazy('employee:password')

    success_message = _('Updated Employee Password.')


class Profile(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    form_class = forms.FormEdit

    template_name = 'employee/edit.html'

    success_message = _('Updated Employee Profile.')

    def get_object(self, queryset=None):
        return get_object_or_404(models.Account, pk=self.kwargs['pk'], is_staff=True)

    def get_success_url(self):
        return reverse_lazy('employee:edit', kwargs={'pk': self.kwargs['pk']})


class Search(LoginRequiredMixin, generic.ListView):
    template_name = 'employee/search.html'

    queryset = models.Account.objects.filter(is_staff=True, is_superuser=False)
