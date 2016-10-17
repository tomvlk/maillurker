from .base import *

####
# Cache & Templates
####
TEMPLATE_LOADERS = (
	('django.template.loaders.cached.Loader', (
		'django.template.loaders.filesystem.Loader',
		'django.template.loaders.app_directories.Loader',
	)),
)

####
# Logging
####
LOGGING = {
	'version': 1,
	'disable_existing_loggers': False,
	'formatters': {
		'verbose': {
			'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
			'datefmt': "%d/%b/%Y %H:%M:%S"
		},
		'simple': {
			'format': '%(levelname)s %(message)s'
		},
	},
	'handlers': {
		'file': {
			'level': 'DEBUG',
			'class': 'logging.FileHandler',
			'filename': 'debug.log',
			'formatter': 'verbose'
		},
	},
	'loggers': {
		'apps': {
			'handlers': ['file'],
			'level': 'DEBUG',
		},
	}
}
