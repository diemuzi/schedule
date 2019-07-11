"""
Database Configuration
"""

# Databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'schedule',
        'USER': 'schedule_user',
        'PASSWORD': 'password',
        'HOST': '10.1.1.1',
        'PORT': 5432,
        'TEST': {
            'NAME': 'test_schedule'
        },
        'ATOMIC_REQUESTS': True
    },
    'default_slave1': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'schedule',
        'USER': 'schedule_user',
        'PASSWORD': 'password',
        'HOST': '10.1.1.1',
        'PORT': 5432,
        'TEST': {
            'MIRROR': 'default'
        },
        'ATOMIC_REQUESTS': False
    }
}

# Database Routers
DATABASE_ROUTERS = [
    'schedule.database.router.MasterSlave'
]
