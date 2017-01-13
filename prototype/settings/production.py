import os
import dj_database_url
from prototype.settings.base import *

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

SECRET_KEY = os.environ['SECRET_KEY']
DEBUG = False

# Databases
DATABASES['default'] = dj_database_url.config()

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

#ADMINS = (('Guilherme Latrova','guilhermelatrova@hotmail.com'),)

# Static files
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)