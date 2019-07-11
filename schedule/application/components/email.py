"""
Email Settings
"""

# Hostname
EMAIL_HOST = 'smtp.mailtrap.io'

# Username
EMAIL_HOST_USER = 'username'

# Password
EMAIL_HOST_PASSWORD = 'password'

# Port
EMAIL_PORT = 2525

# TLS Support
EMAIL_USE_TLS = False

# From Email Address
DEFAULT_FROM_EMAIL = 'noreply@example.com'

#
# Set the administrator email address(es)
#
# Only used when important notications need to be sent
# Example; Queue failed to process
#
# For more than 1 admin, recommended to use a mailing list address here
ADMINS = [
    'user@example.com'
]

#
# Set the manager email address(es)
#
# Only used when DEBUG is False
# Example; 404 Errors
#
# For more than 1 manager, recommended to use a mailing list address here
MANAGERS = [
    'user@example.com'
]
