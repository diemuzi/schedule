from django.contrib import messages
from django.contrib.auth import models as auth_models
from django.db.models import Q
from django.utils.translation import activate
from django.utils.translation import gettext as _


def create_group_permissions(sender, **kwargs):
    group, created = auth_models.Group.objects.get_or_create(name='Client')

    permissions = auth_models.Permission.objects.filter(
        Q(content_type__app_label='login') | Q(content_type__model='comment'))

    for item in permissions:
        group.permissions.add(item.pk)


def handle_login(sender, request, user, **kwargs):
    request.session['django_language'] = user.locale
    request.session['django_timezone'] = user.time_zone

    activate(user.locale)

    messages.add_message(request, messages.INFO, _('Welcome back %s!' % user))


def handle_logout(sender, request, **kwargs):
    messages.add_message(request, messages.INFO, _('You have been logged out.'))
