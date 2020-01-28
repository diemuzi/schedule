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
    'form.apps.FormConfig',
    'locality.apps.LocalityConfig',
    'template.apps.TemplateConfig'
])

# Project Applications
INSTALLED_APPS.extend([
    'asset.apps.AssetConfig',
    'login.apps.LoginConfig',
    'roster.apps.RosterConfig'
])
