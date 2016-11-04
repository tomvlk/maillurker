TEST = True

# Generate unique secret key.
SECRET_KEY = '7=999^z!d6ysczgfsdfa3got@u$5b$hhew=24!m27f_c$-+x7mm*'

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
