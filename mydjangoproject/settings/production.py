"""
See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/
for production-suitable settings.
"""
from .base import *

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES = {
    'default': dj_database_url.config()
}

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers (must have a value when DEBUG is off)
ALLOWED_HOSTS = ['*']
