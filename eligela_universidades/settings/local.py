from .base import *


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3k37ir3&11a2of5d(ro6p)=bau9pgsq(@+p#b#ci7pbehm0au*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

THIRD_PARTY_APPS_LOCAL = (
    'debug_toolbar',
)

INSTALLED_APPS += THIRD_PARTY_APPS_LOCAL


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR.child('db.sqlite3'),
    }
}
