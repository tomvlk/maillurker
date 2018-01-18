from datetime import timedelta

# Allowed hosts
ALLOWED_HOSTS = (
	'maillurker.example.nl',
)

# Generate unique secret key.
SECRET_KEY = 'changeme'

# Enable API tokens for all users
USER_API_KEYS = True

# Turn debug on or off
DEBUG = False

# Authentication options. See example for details
# See http://psa.matiasaguirre.net/docs/index.html for details on social authentication configuration.
AUTHENTICATION = {
	'allow_readonly': False,
	'social': {
		'enabled': True,
		'backends': (
			# Enable your backends here. Note! Only GoogleOAuth2 is fully tested!
			'social_core.backends.google.GoogleOAuth2',
			'social_core.backends.github.GithubOAuth2',
			'social_core.backends.bitbucket.BitbucketOAuth2',
			'social_core.backends.facebook.FacebookOAuth2',
			# 'social_core.backends.dropbox.DropboxOAuth2',
			# 'social_core.backends.flickr.FlickrOAuth',
			# 'social_core.backends.instagram.InstagramOAuth2',
			# 'social_core.backends.live.LiveOAuth2',
			# 'social_core.backends.linkedin.LinkedinOAuth2',
			# 'social_core.backends.odnoklassniki.OdnoklassnikiOAuth2',
			# 'social_core.backends.reddit.RedditOAuth2',
			# 'social_core.backends.soundcloud.SoundcloudOAuth2',
			# 'social_core.backends.tumblr.TumblrOAuth',
			# 'social_core.backends.twitter.TwitterOAuth',
			# 'social_core.backends.vk.VKOAuth2',
			# 'social_core.backends.yahoo.YahooOAuth',
		),
		'options': {
			'SOCIAL_AUTH_GOOGLE_OAUTH2_KEY': 'key.apps.goog...',
			'SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET': 'secret',
			# 'SOCIAL_AUTH_GOOGLE_OAUTH2_WHITELISTED_DOMAINS': [ # Optional, only to ristrict organisation emails.
			# 	'example.com'
			# ],
			'SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE': [
				'https://www.googleapis.com/auth/userinfo.email',
				'https://www.googleapis.com/auth/userinfo.profile'
			],

			'SOCIAL_AUTH_GITHUB_KEY': '',
			'SOCIAL_AUTH_GITHUB_SECRET': '',

			'SOCIAL_AUTH_BITBUCKET_OAUTH2_KEY': '',
			'SOCIAL_AUTH_BITBUCKET_OAUTH2_SECRET': '',

			'SOCIAL_AUTH_FACEBOOK_KEY': '',
			'SOCIAL_AUTH_FACEBOOK_SECRET': '',
		}
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
