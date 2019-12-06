from django.contrib.admin import forms as admin_forms
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views import generic

from login import forms
from login import models
from login.mixin import GaclMixin


class Access(GaclMixin, generic.ListView):
    permission_required = (
        'login.view_accesslog'
    )

    template_name = 'login/access.html'

    ordering = '-date_from'

    paginate_by = 10

    def get_queryset(self):
        return models.AccessLog.objects.filter(account_id=self.request.user.id)


class Index(SuccessMessageMixin, LoginView):
    template_name = 'login/login.html'

    form_class = admin_forms.AuthenticationForm


class Create(SuccessMessageMixin, generic.CreateView):
    template_name = 'login/create.html'

    form_class = forms.FormCreate

    success_url = reverse_lazy('login:login')

    success_message = _('Thank you for registering. Check your email for your login information.')
