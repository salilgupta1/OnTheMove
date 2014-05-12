from settings import *

DEBUG = False
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['*']

ADMINS = (
    ('Salil Gupta', 'salil.gupta323@gmail.com'),
)

MANAGERS = ADMINS

import dj_database_url
DATABASES['default'] =  dj_database_url.config()

INSTALLED_APPS = INSTALLED_APPS + (
    'raven.contrib.django.raven_compat',
)