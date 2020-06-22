"""
Database Configuration
"""

import os

from django.conf import settings

# Default Name
try:
    DATABASE_DEFAULT_NAME = os.environ['DATABASE_DEFAULT_NAME']
except KeyError:
    DATABASE_DEFAULT_NAME = settings.DATABASE_DEFAULT_NAME

# Default Username
try:
    DATABASE_DEFAULT_USER = os.environ['DATABASE_DEFAULT_USER']
except KeyError:
    DATABASE_DEFAULT_USER = settings.DATABASE_DEFAULT_USER

# Default Password
try:
    DATABASE_DEFAULT_PASS = os.environ['DATABASE_DEFAULT_PASS']
except KeyError:
    DATABASE_DEFAULT_PASS = settings.DATABASE_DEFAULT_PASS

# Default Hostname
try:
    DATABASE_DEFAULT_HOST = os.environ['DATABASE_DEFAULT_HOST']
except KeyError:
    DATABASE_DEFAULT_HOST = settings.DATABASE_DEFAULT_HOST

# Read 1 Name
try:
    DATABASE_READ1_NAME = os.environ['DATABASE_READ1_NAME']
except KeyError:
    DATABASE_READ1_NAME = settings.DATABASE_READ1_NAME

# Read 1 Username
try:
    DATABASE_READ1_USER = os.environ['DATABASE_READ1_USER']
except KeyError:
    DATABASE_READ1_USER = settings.DATABASE_READ1_USER

# Read 1 Password
try:
    DATABASE_READ1_PASS = os.environ['DATABASE_READ1_PASS']
except KeyError:
    DATABASE_READ1_PASS = settings.DATABASE_READ1_PASS

# Read 1 Hostname
try:
    DATABASE_READ1_HOST = os.environ['DATABASE_READ1_HOST']
except KeyError:
    DATABASE_READ1_HOST = settings.DATABASE_READ1_HOST

# Databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': DATABASE_DEFAULT_NAME,
        'USER': DATABASE_DEFAULT_USER,
        'PASSWORD': DATABASE_DEFAULT_PASS,
        'HOST': DATABASE_DEFAULT_HOST,
        'PORT': 5432,
        'TEST': {
            'NAME': 'test_' + DATABASE_DEFAULT_NAME
        },
        'ATOMIC_REQUESTS': True
    },
    'default_read1': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': DATABASE_READ1_NAME,
        'USER': DATABASE_READ1_USER,
        'PASSWORD': DATABASE_READ1_PASS,
        'HOST': DATABASE_READ1_HOST,
        'PORT': 5432,
        'TEST': {
            'MIRROR': 'default'
        },
        'ATOMIC_REQUESTS': False
    }
}

# Database Routers
DATABASE_ROUTERS = [
    'database.router.MasterRouter'
]
