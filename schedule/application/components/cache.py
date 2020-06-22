"""
Cache
"""

import os

from django.conf import settings

try:
    CACHE_BACKEND = os.environ['CACHE_BACKEND']
except KeyError:
    CACHE_BACKEND = settings.CACHE_BACKEND

try:
    CACHE_LOCATION = os.environ['CACHE_LOCATION']
except KeyError:
    CACHE_LOCATION = settings.CACHE_LOCATION

# Cache Backends
CACHES = {
    'default': {
        'BACKEND': CACHE_BACKEND,
        'LOCATION': CACHE_LOCATION,
        'OPTIONS': {}
    }
}
