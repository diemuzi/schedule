from django.utils.translation import gettext as _


def breadcrumbs():
    """
    Breadcrumbs

    :return: dict
    """

    return {
        'namespace': 'login',
        'label': _('Login'),
        'pages': [
            {
                'label': _('Create Employee'),
                'url_name': 'create'
            },
            {
                'label': _('Change Password'),
                'url_name': 'password'
            }
        ]
    }
