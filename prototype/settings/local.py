from prototype.settings.base import *

SECRET_KEY = '5a2619d6-dfbd-4b94-8fd4-cffa35cac9c3'
DEBUG = True
ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}'''

import dj_database_url
DATABASES['default'] = dj_database_url.config()