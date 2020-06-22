"""
Email Settings
"""

import os

from django.conf import settings

# Hostname
try:
    EMAIL_HOST = os.environ['EMAIL_HOST']
except KeyError:
    EMAIL_HOST = settings.EMAIL_HOST

# Username
try:
    EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
except KeyError:
    EMAIL_HOST_USER = settings.EMAIL_HOST_USER

# Password
try:
    EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
except KeyError:
    EMAIL_HOST_PASSWORD = settings.EMAIL_HOST_PASSWORD

# Port
try:
    EMAIL_PORT = os.environ['EMAIL_PORT']
except KeyError:
    EMAIL_PORT = settings.EMAIL_PORT

# TLS Support
try:
    EMAIL_USE_TLS = os.environ['EMAIL_USE_TLS']
except KeyError:
    EMAIL_USE_TLS = settings.EMAIL_USE_TLS

# From Email Address
try:
    DEFAULT_FROM_EMAIL = os.environ['EMAIL_DEFAULT_FROM_EMAIL']
except KeyError:
    DEFAULT_FROM_EMAIL = settings.EMAIL_DEFAULT_FROM_EMAIL

# Backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

#
# Set the administrator email address(es)
#
# Only used when important notications need to be sent
# Example; Queue failed to process
#
# For more than 1 admin, recommended to use a mailing list address here
try:
    EMAIL_ADMINS = os.environ['EMAIL_ADMINS']
except KeyError:
    EMAIL_ADMINS = settings.EMAIL_ADMINS

#
# Set the manager email address(es)
#
# Only used when DEBUG is False
# Example; 404 Errors
#
# For more than 1 manager, recommended to use a mailing list address here
try:
    EMAIL_MANAGERS = os.environ['EMAIL_MANAGERS']
except KeyError:
    EMAIL_MANAGERS = settings.EMAIL_MANAGERS
