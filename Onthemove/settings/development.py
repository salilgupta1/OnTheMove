from common import *
import config

SECRET_KEY = config.keys['DJANGO_SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "onthemove",
        "USER": "",
        "PASSWORD": "",
        "HOST": "localhost",
        "PORT": "",
    }
}


EMAIL_HOST_USER = config.keys['SENDGRID_USERNAME']
EMAIL_HOST_PASSWORD = config.keys['SENDGRID_PASSWORD']
