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

if not hasattr(local, 'AUTHENTICATION'):
	raise Exception('Local configuration should contain AUTHENTICATION entry!')

# Generic
TIME_ZONE = 'UTC'

USE_TZ = True
USE_I18N = True
USE_L10N = True

LANGUAGE_CODE = 'en-en'

SECRET_KEY = local.SECRET_KEY
API_KEY = local.API_KEY

if SECRET_KEY == 'changeme' or API_KEY == 'changeme':
	print('YOU SHOULD CHANGE YOUR SECRET KEY AND/OR API KEY!!!')

####
# Mail Server Settings
####
SMTPD_ADDRESS = getattr(local, 'SMTPD_ADDRESS', '0.0.0.0')
SMTPD_PORT = getattr(local, 'SMTPD_PORT', 1025)

# Mail Forwarding policy and settings.
FORWARDING = local.FORWARDING
FORWARDING_ENABLED = bool(FORWARDING['enabled'])
FORWARDING_AUTO = bool(FORWARDING['automatically'])

if FORWARDING_ENABLED and FORWARDING['method'] == 'smtp':
	EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
	EMAIL_HOST = FORWARDING['smtp']['host']
	EMAIL_PORT = FORWARDING['smtp']['port']
	EMAIL_TIMEOUT = FORWARDING['smtp']['timeout']

	if FORWARDING['smtp']['authentication']['enabled']:
		EMAIL_HOST_USER = FORWARDING['smtp']['authentication']['username']
		EMAIL_HOST_PASSWORD = FORWARDING['smtp']['authentication']['password']

	EMAIL_USE_TLS = FORWARDING['smtp']['use_tls']
	EMAIL_USE_SSL = FORWARDING['smtp']['use_ssl']
	EMAIL_SSL_CERTFILE = FORWARDING['smtp']['ssl_certfile']
	EMAIL_SSL_KEYFILE = FORWARDING['smtp']['ssl_keyfile']
else:
	EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

####
# Apps
####
INSTALLED_APPS = [
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
]

# Add app for social login.
if 'social' in local.AUTHENTICATION and type(local.AUTHENTICATION['social']) is dict:
	INSTALLED_APPS.append('social.apps.django_app.default')

# Add source apps
INSTALLED_APPS += [
	'apps.core.apps.CoreConfig',
	'apps.accounts.apps.AccountsConfig',

	'apps.mails.apps.MailsConfig',
	'apps.filters.apps.FiltersConfig',
	'apps.api.apps.ApiConfig',
]

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

# Add social processors
SOCIAL_ENABLED = False
if 'social' in local.AUTHENTICATION and 'enabled' in local.AUTHENTICATION['social'] and local.AUTHENTICATION['social'][
	'enabled']:
	SOCIAL_ENABLED = True

	TEMPLATE_CONTEXT_PROCESSORS += (
		'social.apps.django_app.context_processors.login_redirect',
		'social.apps.django_app.context_processors.backends',
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
	'apps.accounts.middleware.SocialAuthExceptionMiddleware',
)

####
# Authentication and security
####
CORS_ORIGIN_ALLOW_ALL = True

GRAPPELLI_ADMIN_TITLE = 'Mail Lurker, Mail catcher for large environments.'

LOGIN_EXEMPT_URLS = [
	'login/.*',
	'complete/.*',

	'api/.*',
]

# If read-only is enabled, exempt the root.
if 'allow_readonly' in local.AUTHENTICATION and local.AUTHENTICATION['allow_readonly']:
	LOGIN_EXEMPT_URLS += [
		'.*'
	]

AUTHENTICATION_BACKENDS = (
	'django.contrib.auth.backends.ModelBackend',
)

# Add social backends.
SOCIAL_BACKENDS = list()
if SOCIAL_ENABLED and 'backends' in local.AUTHENTICATION['social']:
	AUTHENTICATION_BACKENDS += local.AUTHENTICATION['social']['backends']
	SOCIAL_BACKENDS = local.AUTHENTICATION['social']['backends']

# Add default social options
if SOCIAL_ENABLED:
	SOCIAL_AUTH_STRATEGY = 'social.strategies.django_strategy.DjangoStrategy'
	SOCIAL_AUTH_STORAGE = 'social.apps.django_app.default.models.DjangoStorage'

	SOCIAL_AUTH_PIPELINE = (
		'social.pipeline.social_auth.social_details',
		'social.pipeline.social_auth.social_uid',
		'social.pipeline.social_auth.auth_allowed',
		'social.pipeline.social_auth.social_user',
		'social.pipeline.social_auth.associate_by_email',
		'social.pipeline.user.get_username',
		'social.pipeline.user.create_user',
		'social.pipeline.social_auth.associate_user',
		'social.pipeline.social_auth.load_extra_data',
		'social.pipeline.user.user_details',
	)

# Add social pipelines
if SOCIAL_ENABLED and 'pipelines' in local.AUTHENTICATION['social']:
	SOCIAL_AUTH_PIPELINE = local.AUTHENTICATION['social']['pipelines']

# Add custom social options
if SOCIAL_ENABLED and 'options' in local.AUTHENTICATION['social']:
	locals().update(local.AUTHENTICATION['social']['options'])

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
DATABASES = local.DATABASES

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

####
# OVERRIDES
####
try:
	from .overrides import *
except ImportError as e:
	pass
