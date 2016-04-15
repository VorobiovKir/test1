"""
HEROKU APPLICATION SETTINGS
==========================

The main purpose of this file is to contain those settings that are (potentially)
dependent on the actual environment on which the application is to be deployed.

For the actual (default) settings of Django itself please consult the
settings.py that is included as part of the "*_site" folder in question.
"""

# Determine the root location of the project itself
import os.path

# The default database configuration using dj_database_url.
import dj_database_url

BASE_DIR = os.path.dirname(os.path.abspath(os.path.join(__file__, os.path.pardir)))

# Whether or not to have the application output additional debug
# information when running or encountering an error condition
DEBUG = False

# Enable basic authentication
BASICAUTH_ENABLED = True
BASICAUTH_USERNAME = 'minimax'
BASICAUTH_PASSWORD = 'minimax6524!'

# Whether or not to have the application output additional debug information
# whenever the application encounters a syntax error within one of its templates
TEMPLATE_DEBUG = False

# The list of people who'll receive e-mail notifications whenever
# Django encounters an unexpected error condition at runtime
ADMINS = (
    ('Minimax CMS Support', 'minimax-cms-support@kreios.lu'),
)

DATABASES = {
    'default': dj_database_url.config(),
}

# Settings for the Django e-mail notifications (logging).
# E-mails will be sent to all addresses listed as ADMINS (see above).
EMAIL_HOST = os.environ.get('EMAIL_HOST', '')
EMAIL_PORT = os.environ.get('EMAIL_PORT', 0)
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS', False)
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')
EMAIL_SUBJECT_PREFIX = os.environ.get('EMAIL_SUBJECT_PREFIX', '')

# Make this unique, and don't share it with anybody.
SECRET_KEY = '98&amp;om_!e9kchav8n-l^+!qaq9c3225*2i^b24ji-w==h+c-nwq'
