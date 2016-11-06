from datetime import timedelta

TEST = True

# Generate unique secret key.
SECRET_KEY = '7=999^z!d6ysczgfsdfa3got@u$5b$hhew=24!m27f_c$-+x7mm*'

# Enable API tokens for all users
USER_API_KEYS = True

# Turn debug on or off
DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Authentication options. See example for details
# See http://psa.matiasaguirre.net/docs/index.html for details on social authentication configuration.
AUTHENTICATION = {
	'allow_readonly': False,
	'social': {
		'enabled': False,
	}
}

# Forwarding settings
FORWARDING = {
	# Enable forwarding functionality.
	'enabled': False,

	# Enable automatic forwarding of emails (act as a proxy).
	'automatically': False,

	# Use method for delivering. Choose from 'smtp' / None
	'method': 'smtp',

	# SMTP Smarthost configuration
	'smtp': {
		'host': '127.0.0.1',
		'port': 25,
		'authentication': {
			'enabled': False,
			'username': '',
			'password': '',
		},
		'use_tls': False,
		'use_ssl': False,
		'timeout': None,
		'ssl_keyfile': None,
		'ssl_certfile': None,
	},
}

# Cleanup and remove messages after interval given, False to disable.
# CLEANUP_AFTER = False
CLEANUP_AFTER = timedelta(days=31)


# Enable if you are using a reverse proxy with HTTPS served to the client.
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# SECURE_FORCE = True

# Database
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'lurker',
		'USER': 'root',
		'PASSWORD': '',
		'HOST': 'localhost',
		'PORT': '3306',
	}
}
