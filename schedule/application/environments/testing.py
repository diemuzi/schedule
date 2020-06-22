"""
Testing Override Settings
"""

import os

from django.conf import settings

# Debug
DEBUG = True

# Allowed Hosts
try:
    ALLOWED_HOSTS = [
        os.environ['ALLOWED_HOSTS']
    ]
except KeyError:
    ALLOWED_HOSTS = [
        settings.ALLOWED_HOSTS
    ]

# Site ID
SITE_ID = 1

# Test Runner
TEST_RUNNER = 'django.test.runner.DiscoverRunner'
