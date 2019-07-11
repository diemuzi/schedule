from django.utils.translation import gettext as _


def breadcrumbs():
    """
    Breadcrumbs

    :return: dict
    """

    return {
        'namespace': 'login',
        'label': _('Login'),
        'pages': []
    }
