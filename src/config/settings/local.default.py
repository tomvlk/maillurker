
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
		'enabled': True,
		'backends': (
			'social.backends.google.GoogleOAuth2',
		),
		'options': {
			'SOCIAL_AUTH_GOOGLE_OAUTH2_KEY': 'key.apps.goog...',
			'SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET': 'secret',
			'SOCIAL_AUTH_GOOGLE_OAUTH2_WHITELISTED_DOMAINS': [
				'example.com'
			],
			'SOCIAL_AUTH_GOOGLE_OAUTH_SCOPE': [
				'https://www.googleapis.com/auth/userinfo.email',
				'https://www.googleapis.com/auth/userinfo.profile'
			],
		}
	}
}

# Enable if you are using a reverse proxy with HTTPS served to the client.
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_FORCE = True

# Database
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'maillurker',
		'USER': 'root',
		'PASSWORD': '',
		'HOST': 'localhost',
		'PORT': '3306',
	}
}
