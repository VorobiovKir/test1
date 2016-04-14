"""
DEFAULT APPLICATION SETTINGS
============================

The default applications settings shared by both the development as well as
the production deployment scenario. These settings are normally more or less
agnostic of the specific host environment used during the installation.
"""

import sys
import os.path

# A list of strings representing the host/domain names that this Django site can serve.
# This is a security measure to prevent an attacker from poisoning caches and password
# reset emails with links to malicious hosts by submitting requests with a fake HTTP
# Host header, which is possible even under many seemingly-safe webserver configurations.
# When DEBUG is True or when running tests, host validation is disabled; any host will
# be accepted. Thus it's usually only necessary to set it in production.
ALLOWED_HOSTS = ['.kreios.lu', '127.0.0.1', 'minimax-cms-staging.herokuapp.com', 'minimax-cms-production.herokuapp.com']

# Determine the root location of the project itself
BASE_DIR = os.path.dirname(os.path.abspath(os.path.join(__file__, os.path.pardir)))

# The title to be displayed in the (Grappelli) admin interface (i.e. Login screen, browser tab title)
GRAPPELLI_ADMIN_TITLE = 'Minimax Website'

# The ID, as an integer, of the current site in the django_site database
# table. This is used so that application data can hook into specific
# site(s) and a single database can manage content for multiple sites.
SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Whether or not to have the application output additional debug
# information when running or encountering an error condition
DEBUG = False

# Whether or not to have the application output additional debug information
# whenever the application encounters a syntax error within one of its templates
TEMPLATE_DEBUG = False

# The list of people who'll receive e-mail notifications whenever
# Django encounters an unexpected error condition at runtime
ADMINS = (
    ('Minimax Support', os.environ.get('NOTIFICATION_EMAIL_RECEIVER', 'info@kreios.lu')),
)

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en'

# Possible languages enabled for this installation
gettext = lambda s: s
LANGUAGES = (
    ('en', gettext('English')),
    ('de', gettext('German')),
)

# A string representing the full Python import path to your root URL configuration
ROOT_URLCONF = 'minimax_site.urls'

# The custom dashboard to display at the root level of our admin interface
GRAPPELLI_INDEX_DASHBOARD = 'minimax.dashboard.CustomIndexDashboard'

# The list of IP addresses that the Django debug toolbar should be made visible to
INTERNAL_IPS = ('127.0.0.1',)

# Configuration specific to the Django Debug Toolbar add-on
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}

# Default time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'UTC' if sys.platform not in ('win32', 'cygwin') else 'Europe/Luxembourg'

# Absolute file system path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" sub directories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# The file storage engine to use when collecting static files. GzipManifestStaticFilesStorage
# facilitates 'cache busting' by appending the MD5 hash of the file's content to its filename.
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

# How long non-versioned files (i.e. those without cache buster) should be cached by the
# browser or CDN (via "Cache-Control:public, max-age=XXXX")
WHITENOISE_MAX_AGE = 600

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# List of locations of the template source files searched by
# django.template.loaders.filesystem.Loader (in search order)
TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)


# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
        'minimax.loaders.Loader',
    )),
)

# What Django middleware to enable for this site
MIDDLEWARE_CLASSES = (
    'minimax_site.middleware.BasicAuthMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'minimax_site.middleware.AdminForceEnglishMiddleware',
)

# A tuple of callables that are used to populate the context in RequestContext.
# These callables take a request object as their argument and return a dictionary
# of items to be merged into the context.
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages'
)

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'wsgi.application'

# Application installed so far
INSTALLED_APPS = (
    'minimax',
    'grappelli.dashboard',
    'modeltranslation',
    'grappelli',
    'reversion',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django_extensions',
    'avatar',
    'gunicorn',
    'debug_toolbar',
    'django_object_actions',
    'mptt',
    'storages',
    's3direct'
)

MIME_TYPE_IMAGE = ['image/jpeg', 'image/png', 'image/gif']
MIME_TYPE_TEXT = ['text/plain', 'text/richtext', 'text/csv', 'application/rtf']
MIME_TYPE_ARCHIVE = ['application/zip', 'application/rar', 'application/x-7z-compressed']
MIME_TYPE_PDF = ['application/pdf']
MIME_TYPE_OFFICE = ['application/msword', 'application/vnd.ms-powerpoint', 'application/vnd.ms-excel',
                    'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
                    'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                    'application/vnd.openxmlformats-officedocument.presentationml.presentation',
                    # OpenOffice formats
                    'application/vnd.oasis.opendocument.text', 'application/vnd.oasis.opendocument.presentation',
                    'application/vnd.oasis.opendocument.spreadsheet']

# Use Amazon S3 for storage for uploaded media files.
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID', '')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY', '')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME', '')

# S3Direct upload settings
S3DIRECT_REGION = os.environ.get('AWS_BUCKET_REGION', 'eu-central-1')
S3DIRECT_DESTINATIONS = {
    'page_content': ('uploads/page_content', lambda u: True, MIME_TYPE_IMAGE),
    'news': ('uploads/news', lambda u: True, MIME_TYPE_IMAGE),
    'employees': ('uploads/employees', lambda u: True, MIME_TYPE_IMAGE),
    'applications': ('uploads/applications', lambda u: True, MIME_TYPE_IMAGE),
    'certification_types': ('uploads/certification_types', lambda u: True, MIME_TYPE_IMAGE),
    'customers': ('uploads/customers', lambda u: True, MIME_TYPE_IMAGE),
    'page_banner': ('uploads/page_banner', lambda u: True, MIME_TYPE_IMAGE),
    'technologies': ('uploads/technologies', lambda u: True, MIME_TYPE_IMAGE),
    'solutions': ('uploads/solutions', lambda u: True, MIME_TYPE_IMAGE),
    'documents': ('uploads/documents', lambda u: True, MIME_TYPE_IMAGE + MIME_TYPE_TEXT + MIME_TYPE_ARCHIVE +
                  MIME_TYPE_PDF + MIME_TYPE_OFFICE),
}

###################################
# Model Translation
###################################

# Include custom model fields for translation
MODELTRANSLATION_CUSTOM_FIELDS = (
    'S3DirectField',
)

MODELTRANSLATION_FALLBACK_LANGUAGES = {'default': ('en', 'de'), 'en': ('de', )}

###################################
# Logging configuration
###################################

# This site's logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(asctime)s %(message)s'
        },
        },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'django.utils.log.NullHandler',
            },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
            },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
            },
        }
}

###################################
# Avatar handling
###################################

# Django-avatar configuration item:
# A boolean determining whether to default to the Gravatar service if no Avatar instance is found in the system
# for the given user. Defaults to True.
AVATAR_GRAVATAR_BACKUP = False

# Django-avatar configuration item:
# The default URL (being appended to the static root) to default to if AVATAR_GRAVATAR_BACKUP is set to False and
# there is no Avatar instance found in the system for the given user.
AVATAR_DEFAULT_URL = 'minimax/images/default-avatar.png'

###################################
# Branding specific configuration
###################################

# The CSS file providing the color, logo, etc. information of the overall back-end. The referenced file is expected
# to live in the static folder.
CSS_BRANDING_FILE = 'minimax/css/branding.css'

# The FAVICON to referenced from the HTML header. The referenced file is expected to live in the static folder
FAVICON_FILE = 'minimax/images/favicon.ico'

###################################
# Functionality: local.settings.py
###################################

# Finally, we'll overload default with local settings
try:
    if 'DYNO' in os.environ.keys():
        from heroku_settings import *  # @UnusedWildImport
    else:
        from local_settings import *  # @UnusedWildImport
except ImportError:
    import sys
    sys.exit('Failed to locate and load additional [env]_settings.py; did you perhaps forget to create your '
             'local_settings.py yet (e.g. using one of the available templates)?')
