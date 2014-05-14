from common import *

DEBUG = False
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['onthemove.herokuapp.com']

ADMINS = (
    ('Salil Gupta', 'salil.gupta323@gmail.com'),
)

MANAGERS = ADMINS

import dj_database_url
DATABASES['default'] = dj_database_url.config()

INSTALLED_APPS = INSTALLED_APPS + (
    'raven.contrib.django.raven_compat',
)

import os

SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

EMAIL_HOST_USER = os.environ['SENDGRID_USERNAME']
EMAIL_HOST_PASSWORD = os.environ['SENDGRID_PASSWORD']