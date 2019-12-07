from django.apps import AppConfig
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from gwhcp.contrib.template.templatetags.template_breadcrumb import nav

from roster import navigation


class RosterConfig(AppConfig):
    name = 'roster'

    def ready(self):
        from roster import signals

        nav.append(navigation.breadcrumbs())

        post_save.connect(signals.create_roster, sender=get_user_model())
