"""Settings for Development Server"""
from .base import *

####
# Add debug apps.
####

INSTALLED_APPS += [
	'debug_toolbar',
]

STRONGHOLD_PUBLIC_URLS += [
	'__debug__',
]

MIDDLEWARE += [
	'debug_toolbar.middleware.DebugToolbarMiddleware',
]

####
# Broker
####
BROKER_URL = 'django://'

####
LOGGING = {
	'version': 1,
	'formatters': {
		'color_console': {
			'()': 'colorlog.ColoredFormatter',
			'format': '%(log_color)s%(levelname)-8s [%(name)s:%(lineno)s]%(reset)s %(blue)s %(message)s',
			'datefmt': "%d/%b/%Y %H:%M:%S",
			'log_colors': {
				'DEBUG': 'cyan',
				'INFO': 'green',
				'WARNING': 'yellow',
				'ERROR': 'red',
				'CRITICAL': 'red',
			},
		},
	},
	'filters': {
		'require_debug_true': {
			'()': 'django.utils.log.RequireDebugTrue',
		}
	},
	'handlers': {
		'console': {
			'level': 'DEBUG',
			'filters': ['require_debug_true'],
			'class': 'logging.StreamHandler',
			'formatter': 'color_console',
		}
	},
	'loggers': {
		'apps': {
			'level': 'DEBUG',
			'handlers': ['console'],
		},
		'werkzeug': {
			'handlers': ['console'],
			'level': 'DEBUG',
			'propagate': True,
		},
	}
}

COMPRESS_ENABLED = False
