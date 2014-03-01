"""
Django settings for mydjangoproject project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

import os

# Build paths inside the project with these variables
CONFIG_ROOT = os.path.dirname(os.path.dirname(__file__))
PROJECT_ROOT = os.path.dirname(CONFIG_ROOT)


SECRET_KEY = os.environ['SECRET_KEY']

# Debug should NOT be turned on in production
DEBUG = False
TEMPLATE_DEBUG = False

# See https://docs.djangoproject.com/en/1.6/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/
LANGUAGE_CODE = 'en-ca'
TIME_ZONE = 'America/Toronto'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# See https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_ROOT = os.path.join(CONFIG_ROOT, 'served/static/')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(CONFIG_ROOT, 'served/media/')
MEDIA_URL = '/media/'

STATICFILES_DIRS = (
    os.path.join(CONFIG_ROOT, 'static'),
)

TEMPLATE_DIRS = (
    os.path.join(CONFIG_ROOT, 'templates'),
)


# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'debug_toolbar',
    'south',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'mydjangoproject.urls'

WSGI_APPLICATION = 'mydjangoproject.wsgi.application'
