from .base import *


DEBUG = True
TEMPLATE_DEBUG = True


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mydjangoproject_dev',
        'USER': 'yiqing',
        'PASSWORD': 'yiqing',
        'HOST': '127.0.0.1',
        'PORT': '',
        # autocommit is turned on by default
    }
}

