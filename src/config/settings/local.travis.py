TEST = True

# Database credentials and details
MYSQL_DB = 'lurker'
MYSQL_USERNAME = 'root'
MYSQL_PASSWORD = ''
MYSQL_HOST = 'localhost'
MYSQL_PORT = '3306'

# Generate unique secret key.
SECRET_KEY = '7=999^z!d6ysczgfsdfa3got@u$5b$hhew=24!m27f_c$-+x7mm*'

# Turn debug on or off
DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Activate if you want to secure the whole application with user accounts.
GLOBAL_AUTHENTICATION = False

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

