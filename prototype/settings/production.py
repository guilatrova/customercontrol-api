import os
# Parse database configuration from $DATABASE_URL
import dj_database_url
from prototype.settings.base import *

SECRET_KEY = os.environ['SECRET_KEY']
DEBUG = False
DATABASES['default'] = dj_database_url.config()

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

#ADMINS = (('Guilherme Latrova','guilhermelatrova@hotmail.com'),)