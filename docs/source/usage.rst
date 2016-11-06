Usage
=====

The following sections will give you instructions on how to start the servers and start using the application.

.. note::
    You need to be in an activated virtualenv to execute most of the commands!


Start Gunicorn
--------------

You can start the Gunicorn instance for the application with the following command (make sure you are in the ./src folder):

.. code-block:: bash

    $ gunicorn wsgi:application -c gunicorn.py

To start with a linux socket file:

.. code-block:: bash

    $ gunicorn wsgi:application -c gunicorn.py --bind "unix:gunicorn.socket"

.. seealso::
    For the full documentation and how to run in daemon mode,
    see http://docs.gunicorn.org/en/latest/configure.html#command-line


Start SMTP Server
-----------------

To be able to receive any mails you need to start the SMTP server that listens to messages and will parse and save
all messages that will be send to the SMTP server.

To start the server, execute the following:

.. code-block:: bash

    $ python manage.py start_lurking

.. note::
    The SMTP server doesn't go in daemon/background yet. This is on the roadmap.


Create first user
-----------------

You can create a superuser with the following command:

.. code-block::

    $ python manage.py createsuperuser


Configure Webserver
-------------------

You should configure your webserver to reverse proxy to the Gunicorn server.


Nginx
~~~~~

.. note::
    This part is not yet confirmed to be working or completed.


.. code-block:: nginx

    server {
        listen 80;
        server_name server_domain_or_IP;

        location = /favicon.ico { access_log off; log_not_found off; }
        location /static/ {
            root /home/user/lurker/src;
        }

        location / {
            include proxy_params;
            proxy_pass http://unix:/home/user/lurker/src/gunicorn.sock;
        }
    }

