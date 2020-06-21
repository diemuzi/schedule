from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views import generic

from roster import excel
from roster import forms
from roster import models


class Download(LoginRequiredMixin, generic.View):
    @staticmethod
    def get(request):
        return excel.generate_excel()


class PreviewAll(LoginRequiredMixin, generic.ListView):
    template_name = 'roster/preview_all.html'

    queryset = models.Roster.search_staff()

    ordering = 'account__last_name'


class PreviewEmployee(LoginRequiredMixin, generic.DetailView):
    template_name = 'roster/preview_employee.html'

    model = models.Roster


class Profile(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    form_class = forms.FormProfile

    template_name = 'roster/profile.html'

    success_message = _('Updated employee profile.')

    def get_object(self, queryset=None):
        return get_object_or_404(get_user_model(), pk=self.kwargs['pk'], is_staff=True)

    def get_success_url(self):
        return reverse_lazy('roster:profile', kwargs={'pk': self.kwargs['pk']})


class Schedule(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    form_class = forms.FormSchedule

    template_name = 'roster/schedule.html'

    model = models.Roster

    success_message = _('Updated employee schedule.')

    def get_success_url(self):
        return reverse_lazy('roster:schedule', kwargs={'pk': self.kwargs['pk']})


class Search(LoginRequiredMixin, generic.ListView):
    template_name = 'roster/search.html'

    queryset = get_user_model().objects.filter(is_staff=True, is_superuser=False)

    ordering = ('facility', 'last_name')
