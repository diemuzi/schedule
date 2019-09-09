from django.utils.translation import gettext as _


def breadcrumbs():
    """
    Breadcrumbs

    :return: dict
    """

    return {
        'namespace': 'roster',
        'label': _('Roster'),
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
                'label': _('Preview All Schedules'),
                'url_name': 'preview-all'
            },
            {
                'label': _('Preview Employee Schedule'),
                'url_name': 'preview-employee'
            },
            {
                'label': _('Search Employees'),
                'url_name': 'search'
            }
        ]
    }
