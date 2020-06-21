"""
Cache
"""

import os

# Cache Backends
CACHES = {
    'default': {
        'BACKEND': os.environ['CACHE_BACKEND'],
        'LOCATION': [os.environ['CACHE_LOCATION']],
        'OPTIONS': {}
    }
}
