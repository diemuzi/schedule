from django.apps import AppConfig

from schedule.roster import navigation
from schedule.contrib.template.templatetags.template_breadcrumb import nav


class RosterConfig(AppConfig):
    name = 'schedule.roster'

    def ready(self):
        nav.append(navigation.breadcrumbs())
