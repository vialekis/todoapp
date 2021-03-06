"""
Django settings for todoapp project.

Generated by 'django-admin startproject' using Django 2.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""
import django_heroku
import os
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8=wn5u_6pps6w%4)6jygl=w*5p6s&522ilnu$^2(a_h+l@_xmt'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tasks.apps.TasksConfig',
    'accounts.apps.AccountsConfig',
    'taggit',
    'debug_toolbar',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'todoapp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'todoapp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

# STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,"static"),]
LOGIN_REDIRECT_URL = "tasks:list"
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,"media/")

STATIC_URL = '/asset-v1:Skillfactory+PW-4+APR_15+type@asset+block/a406a22_/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
INTERNAL_IPS = ['127.0.0.1', 'localhost']




# # Local
# EMAIL_HOST = 'smtp.mail.ru'
# EMAIL_HOST_USER = '2702040@mail.ru'
# EMAIL_HOST_PASSWORD = '4rjhjds3'
# EMAIL_PORT = 465
# EMAIL_USE_SSL = True
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# # end local

# Heroku
EMAIL_HOST = os.environ.get("EMAIL_HOST")
EMAIL_USE_SSL = bool(os.environ.get("EMAIL_USE_SSL"))
EMAIL_USE_TLS = bool(os.environ.get("EMAIL_USE_TLS"))
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DISABLE_COLLECTSTATIC=1
SENTRY_DSN = os.environ.get("SENTRY_DSN")
django_heroku.settings(locals())
# EMAIL_PORT = int(os.environ.get("EMAIL_PORT"))
EMAIL_PORT = 465
# # end heroku
sentry_sdk.init(
    dsn=SENTRY_DSN,
    integrations=[DjangoIntegration()])