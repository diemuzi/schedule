from django.apps import AppConfig
from gwhcp.contrib.template.templatetags.template_breadcrumb import nav

from employee import navigation


class EmployeeConfig(AppConfig):
    name = 'employee'

    def ready(self):
        nav.append(navigation.breadcrumbs())

        # noinspection PyUnresolvedReferences
        import employee.signal
