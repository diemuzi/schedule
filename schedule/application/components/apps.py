"""
Applications
"""

# Django Applications
INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.postgres',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles'
]

# Third-Party Applications
INSTALLED_APPS.extend([
    'compressor',
    'widget_tweaks'
])

# Base Applications
INSTALLED_APPS.extend([
    'schedule.contrib.form.apps.FormConfig',
    'schedule.contrib.locality.apps.LocalityConfig',
    'schedule.contrib.template.apps.TemplateConfig'
])

# Project Applications
INSTALLED_APPS.extend([
    'schedule.asset.apps.AssetConfig',
    'schedule.employee.apps.EmployeeConfig',
    'schedule.login.apps.LoginConfig',
    'schedule.roster.apps.RosterConfig'
])
