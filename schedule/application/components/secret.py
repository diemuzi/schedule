"""
Secret Settings
"""

import os

from django.conf import settings

# Secret Key
try:
    SECRET_KEY = os.environ['SECRET_KEY']
except KeyError:
    SECRET_KEY = settings.SECRET_KEY
