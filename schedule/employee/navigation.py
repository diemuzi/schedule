from django.utils.translation import gettext as _


def breadcrumbs():
    """
    Breadcrumbs

    :return: dict
    """

    return {
        'namespace': 'employee',
        'label': _('Employee'),
        'pages': [
            {
                'label': _('Create Employee'),
                'url_name': 'add'
            },
            {
                'label': _('Profile'),
                'url_name': 'edit'
            },
            {
                'label': _('Change Password'),
                'url_name': 'password'
            },
            {
                'label': _('Search Employees'),
                'url_name': 'search'
            }
        ]
    }
