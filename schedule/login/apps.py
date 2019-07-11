from django.apps import AppConfig

from schedule.login import navigation
from schedule.contrib.template.templatetags.template_breadcrumb import nav


class LoginConfig(AppConfig):
    name = 'schedule.login'

    def ready(self):
        nav.append(navigation.breadcrumbs())

        # noinspection PyUnresolvedReferences
        import schedule.login.signals
