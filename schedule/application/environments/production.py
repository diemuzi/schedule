"""
Production Override Settings
"""

import os

from django.conf import settings

# Debug
DEBUG = False

# Allowed Hosts
try:
    ALLOWED_HOSTS = os.environ['ALLOWED_HOSTS']
except KeyError:
    ALLOWED_HOSTS = settings.ALLOWED_HOSTS

# Site ID
SITE_ID = 1
