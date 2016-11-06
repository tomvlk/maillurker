Configure Lurker
================
.. highlight:: python

The following sections will cover all possible configuration options to be configured in the ```local.py``` file.

.. note:: Make sure you have already copied the ``local.default.py`` to ``local.py``. If not
          please see the :doc:`installation sections <installation>`.


Secret Key
----------

This option is very important to change at first installation. The secret key is used in several unique and security
related aspects and is very important you change and keep secure!

.. code-block:: python

    # Generate unique secret key.
    SECRET_KEY = 'changeme'

You can generate a new token by running a special command:

.. code-block:: bash

    $ python manage.py generate_secret_key

.. danger::
    **Make sure you change this before start using the application!**
    Not changing could be devastating when your table with passwords leak and for securing cookies, tokens and sessions.


User API Access
---------------

This option enables the display of a personalized token to the users. Disable if you don't want to display the tokens
to the users on their Account page.

.. code-block:: python

    # Enable API tokens for all users
    USER_API_KEYS = True


Debug Mode
----------

Enable debug mode while developing, will enable several Django related features to investigate some issues.

.. code-block:: python

    DEBUG = False

.. warning::
    Enabling debug mode will show users some insights you may want to hide or you don't want to share. Especially when
    running in reverse proxy (what you shouldn't do).


Authentication
--------------

This part of the configuration is pretty important and can get complicated. It has several options for normal user/pass
authentication but even more settings for the Social Authentication implemented in the application.

The authentication options are all suited inside a ``dict``. Bellow is the most basic setup possible.

.. code-block:: python

    AUTHENTICATION = {
	    'allow_readonly': False,
	    'social': {
		    'enabled': False,
        },
        'backends': [],
        'options': {},
    }


Read Only access
~~~~~~~~~~~~~~~~

You can enable read only access by changing the value of ``allow_readonly`` to ``True``. This will allow to only
read messages and use global filters.


Social enabled
~~~~~~~~~~~~~~

Before the social buttons and the middleware and apps will be used, you have to turn the Social Auth on by changing the
value of the subkey ``enabled`` of ``social`` to ``True``.


Social backends
~~~~~~~~~~~~~~~

To be able to use the Social Authentication, you have to provide a list with backends to use. Currently there is one
that is fully tested and that's used in the following examples.
For a full list and documentation on the backends, see https://python-social-auth.readthedocs.io/

.. code-block:: python

    'backends': (
        'social.backends.google.GoogleOAuth2',
    )


Social options
~~~~~~~~~~~~~~

You can pass any custom social options to the options dict:

.. code-block:: python

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
    }

.. seealso::
    The social authentication has several customizable options, some are not documented here. See the full documentation
    here: https://python-social-auth.readthedocs.io/


Mail Forwarding
---------------

.. warning::
    This feature is not yet completed. Only configuration is known. Some or all functions are not yet implemented!

.. code-block:: python

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



Automatic Cleanup
-----------------

The lurker listening process can automatically cleanup old messages based on a given timedelta.

Default configuration:
.. code-block:: python

    CLEANUP_AFTER = timedelta(days=31)

To disable the function:
.. code-block:: python

    CLEANUP_AFTER = False



Proxy & HTTPS
-------------

If you have configured your webserver with reverse proxy to the gunicorn process and you want to support HTTPS you may
need to change the lines or force the header ``HTTP-X-Forwarded-Proto`` to be present by the webserver. Sometimes you
want to force this behavior with the following lines:

.. code-block:: python

    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SECURE_FORCE = True



Database
--------

The most important one, and the most expandable one too. Configure your database with the standard Django configuration
in the ``DATABASES`` field.

.. code-block:: python

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

This configuration is exactly the same as the Django one. Default and tested is MySQL, but you may also use some other
database engine.

.. seealso::
    https://docs.djangoproject.com/en/1.8/ref/settings/#databases




