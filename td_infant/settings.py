"""
Django settings for td_infant project.


Generated by 'django-admin startproject' using Django 2.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import sys
APP_NAME = 'td_infant'
from pathlib import Path
import configparser
from pathlib import PurePath

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_ID = 40
DEFAULT_STUDY_SITE = '40'

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0s7@cgv8cq9x5(6*#v@=!447wj6a)1ptauvzf$7_1k3(gvn5m%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

CONFIG_FILE = f'{APP_NAME}.conf'
if DEBUG:
    ETC_DIR = str(PurePath(BASE_DIR).joinpath('etc'))
else:
    ETC_DIR = '/etc/'

CONFIG_PATH = ETC_DIR
config = configparser.RawConfigParser()
config.read(os.path.join(CONFIG_PATH, CONFIG_FILE))

HOLIDAY_FILE = os.path.join(BASE_DIR, 'holidays.csv')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django_crypto_fields.apps.AppConfig',
    'edc_protocol.apps.AppConfig',
    'edc_label.apps.AppConfig',
    'edc_lab.apps.AppConfig',
    'edc_locator.apps.AppConfig',
    'edc_export.apps.AppConfig',
    'edc_timepoint.apps.AppConfig',
    'edc_appointment.apps.AppConfig',
    'edc_action_item.apps.AppConfig',
    'td_maternal.apps.AppConfig',
    'td_infant.apps.EdcVisitTrackingAppConfig',
    'td_infant.apps.AppConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'edc_subject_dashboard.middleware.DashboardMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'td_infant.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'td_infant.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# https://docs.djangoproject.com/en/2.0/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'td_infant', 'static')
STATIC_URL = '/static/'
DEVICE_ID = '99'
COUNTRY = 'botswana'
DASHBOARD_URL_NAMES = {
    'subject_listboard_url': 'td_dashboard:subject_listboard_url',
    'subject_dashboard_url': 'td_dashboard:subject_dashboard_url',
}
