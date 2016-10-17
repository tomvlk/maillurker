import os
import pymysql

pymysql.install_as_MySQLdb()

DEBUG = bool(int(os.getenv('DJANGO_IS_DEBUG', True)))

if DEBUG:
	from .dev import *
else:
	from .live import *

# Debug override
DEBUG = bool(int(os.getenv('DJANGO_IS_DEBUG', True)))
TEMPLATE_DEBUG = DEBUG
