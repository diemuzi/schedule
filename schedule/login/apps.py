from django.apps import AppConfig
from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.signals import user_logged_out
from django.db.models.signals import post_migrate
from gwhcp.contrib.template.templatetags.template_breadcrumb import nav

from login import navigation


class LoginConfig(AppConfig):
    name = 'login'

    def ready(self):
        from login import signals

        nav.append(navigation.breadcrumbs())

        post_migrate.connect(signals.create_group_permissions, sender=self)

        user_logged_in.connect(signals.handle_login)
        user_logged_out.connect(signals.handle_logout)
