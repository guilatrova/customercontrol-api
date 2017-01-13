from prototype.settings.base import *

SECRET_KEY = '5a2619d6-dfbd-4b94-8fd4-cffa35cac9c3'
DEBUG = True
ALLOWED_HOSTS = []

# Databases
DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),    
}

# Static files

STATIC_ROOT = posixpath.join(*(BASE_DIR.split(os.path.sep) + ['static']))