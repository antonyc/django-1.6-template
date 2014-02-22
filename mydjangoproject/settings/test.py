from .base import *


# Test database!
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mydjangoproject_test',
        'USER': 'yiqing',
        'PASSWORD': 'yiqing',
        'HOST': '127.0.0.1',
        'PORT': '',  # empty string for default
    },
}
