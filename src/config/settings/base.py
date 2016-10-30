"""Base settings shared by all environments"""

import os

# Import global settings to make it easier to extend settings.
import datetime
from django.conf.global_settings import *

from config.settings import local

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

TMP_DIR = os.path.join(BASE_DIR, 'tmp')
DATA_DIR = os.path.join(os.path.dirname(BASE_DIR), 'data')
TEST_DIR = os.path.join(os.path.dirname(BASE_DIR), 'src', 'test')

try:
	os.makedirs(TMP_DIR)
except Exception:
	pass

# Generic
TIME_ZONE = 'UTC'

USE_TZ = True

USE_I18N = True

USE_L10N = True

LANGUAGE_CODE = 'en-en'

SECRET_KEY = local.SECRET_KEY

####
# Mail Server Settings
####
SMTPD_ADDRESS = getattr(local, 'SMTPD_ADDRESS', '0.0.0.0')
SMTPD_PORT = getattr(local, 'SMTPD_PORT', 1025)

####
# Apps
####
INSTALLED_APPS = (
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'django.contrib.humanize',
	'crispy_forms',
	'material',
	'material.admin',
	'rest_framework',
	'rest_framework.authtoken',
	'compressor',
	'corsheaders',

	'apps.core.apps.CoreConfig',
	'apps.accounts.apps.AccountsConfig',

	'apps.mails.apps.MailsConfig',
	'apps.filters.apps.FiltersConfig',
	'apps.api.apps.ApiConfig',
)

####
# Base Settings and content.
####
ROOT_URLCONF = 'config.urls'
COMPRESS_ENABLED = True

LOGIN_URL = 'accounts:login'
LOGOUT_URL = 'accounts:logout'
LOGIN_REDIRECT_URL = '/'
AUTH_USER_MODEL = 'accounts.User'

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

WSGI_APPLICATION = 'wsgi.application'

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


####
# Templates & Middleware
####
TEMPLATE_CONTEXT_PROCESSORS += (
	'django.core.context_processors.request',
	'django.contrib.messages.context_processors.messages',
	'apps.core.context.add_global_context',
	'apps.filters.context.add_global_context',
	'apps.mails.context.add_global_context',
)

CRISPY_TEMPLATE_PACK = 'bootstrap3'

MIDDLEWARE_CLASSES = (
	'django.contrib.sessions.middleware.SessionMiddleware',

	'corsheaders.middleware.CorsMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',

	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.auth.middleware.SessionAuthenticationMiddleware',

	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',

	'apps.accounts.middleware.LoginRequiredMiddleware',
)


####
# Authentication and security
####
CORS_ORIGIN_ALLOW_ALL = True

GRAPPELLI_ADMIN_TITLE = 'Email Lurker, Email Catcher'

LOGIN_EXEMPT_URLS = [
	'api/.*',
]
if not getattr(local, 'GLOBAL_AUTHENTICATION', False):
	LOGIN_EXEMPT_URLS += [
		'.*'
	]

AUTHENTICATION_BACKENDS = (
	'django.contrib.auth.backends.ModelBackend',
)


####
# Template and cache
####
TEMPLATE_LOADERS = (
	'django.template.loaders.filesystem.Loader',
	'django.template.loaders.app_directories.Loader',
)

STATICFILES_FINDERS = (
	'django.contrib.staticfiles.finders.FileSystemFinder',
	'django.contrib.staticfiles.finders.AppDirectoriesFinder',
	'compressor.finders.CompressorFinder',
)

CACHES = {
	'default': {
		'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
		'LOCATION': 'django_cache',
	}
}


####
# Database settings.
####
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': local.MYSQL_DB,
		'USER': local.MYSQL_USERNAME,
		'PASSWORD': local.MYSQL_PASSWORD,
		'HOST': local.MYSQL_HOST,
		'PORT': local.MYSQL_PORT,
	}
}

####
# API
####
REST_FRAMEWORK = {
	'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAuthenticated',),
	'DEFAULT_RENDERER_CLASSES': (
		'rest_framework.renderers.JSONRenderer',
		'rest_framework.renderers.BrowsableAPIRenderer',
	),
	'DEFAULT_AUTHENTICATION_CLASSES': (
		'rest_framework.authentication.TokenAuthentication',
		'rest_framework.authentication.SessionAuthentication',
	)
}

####
# TEST
####
if getattr(local, 'TEST', False):
	TEST = True
	TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
	TEST_APPS = (
		'apps.accounts',
		'apps.api',
		'apps.core',
		'apps.filters',
		'apps.mails'
	)

	NOSE_ARGS = [
		'--with-coverage',
		'--cover-package={}'.format(','.join(TEST_APPS)),
		'--cover-branches',
	]
