"""
Database Configuration
"""

import os

# Databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['DATABASE_DEFAULT_NAME'],
        'USER': os.environ['DATABASE_DEFAULT_USER'],
        'PASSWORD': os.environ['DATABASE_DEFAULT_PASS'],
        'HOST': os.environ['DATABASE_DEFAULT_HOST'],
        'PORT': 5432,
        'TEST': {
            'NAME': 'test_DATABASE'
        },
        'ATOMIC_REQUESTS': True
    },
    'default_slave1': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['DATABASE_SLAVE_NAME'],
        'USER': os.environ['DATABASE_SLAVE_USER'],
        'PASSWORD': os.environ['DATABASE_SLAVE_PASS'],
        'HOST': os.environ['DATABASE_SLAVE_HOST'],
        'PORT': 5432,
        'TEST': {
            'MIRROR': 'default'
        },
        'ATOMIC_REQUESTS': False
    }
}

# Database Routers
DATABASE_ROUTERS = [
    'database.router.MasterSlave'
]
