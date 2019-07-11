from django.contrib import messages
from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.signals import user_logged_out
from django.dispatch import receiver
from django.utils.translation import activate
from django.utils.translation import gettext as _


@receiver(user_logged_in)
def handle_login(sender, request, user, **kwargs):
    request.session['django_language'] = user.locale
    request.session['django_timezone'] = user.time_zone

    activate(user.locale)

    messages.add_message(request, messages.INFO, _('Welcome back %s!' % user))


@receiver(user_logged_out)
def handle_logout(sender, request, **kwargs):
    messages.add_message(request, messages.INFO, _('You have been logged out.'))
