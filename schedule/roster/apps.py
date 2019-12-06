from django.apps import AppConfig
from gwhcp.contrib.template.templatetags.template_breadcrumb import nav

from roster import navigation


class RosterConfig(AppConfig):
    name = 'roster'

    def ready(self):
        nav.append(navigation.breadcrumbs())
