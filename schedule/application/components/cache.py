"""
Cache
"""

# Cache Backends
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': [],
        'OPTIONS': {}
    }
}
