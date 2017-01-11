import os
from prototype.settings.base import *

SECRET_KEY = os.environ['SECRET_KEY']
DEBUG = False

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')