from base import *

SECRET_KEY = get_env_variable('KANTASKER_SECRET_KEY')

DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

TEST_APPS = (
    'django_nose',
)

INSTALLED_APPS = TEST_APPS + INSTALLED_APPS

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'