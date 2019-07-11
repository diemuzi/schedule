from django.apps import AppConfig

from schedule.employee import navigation
from schedule.contrib.template.templatetags.template_breadcrumb import nav


class EmployeeConfig(AppConfig):
    name = 'schedule.employee'

    def ready(self):
        nav.append(navigation.breadcrumbs())

        # noinspection PyUnresolvedReferences
        import schedule.employee.signal
