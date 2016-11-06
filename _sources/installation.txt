Installation
============

The following sections will instruct you how to install the Mail Lurker. If you only want to upgrade the installation,
just pull, run migrations, collect static files and compress static files.


Install environment
-------------------

Clone the repository into your destination:

.. code-block:: bash

    $ git clone https://github.com/tomvlk/maillurker.git maillurker


Change directory into cloned repository.

.. code-block:: bash

    $ cd maillurker


Create a ``virtualenv`` in the project directory. Depending on your installation this command can be different.

.. code-block:: bash

    $ virtualenv -p python3 env


Activate the virtualenv with:

.. code-block:: bash

    $ source env/bin/activate


Install dependencies with pip and the requirements.txt file:

.. code-block:: bash

    $ pip install -r requirements.txt

Now your environment is ready. You can now go to the next step.


Configuration Files
-------------------

In order to start we need to know some information about the database, the port and address for the SMTP server and the
general configuration. To keep an structured and deployment-easy configuration structure we created a directory django
settings module.

The first setting file to be loaded is ``src/config/settings/__init__.py``. In that file we will decide if we use the
``live.py`` or the ``dev.py`` settings directives. One of the choices will be loaded and after it the ``base.py`` will be
loaded.

After loading the ``base.py`` we will load in any local changed settings (not tracked in git). Those settings must be in
``local.py``, the file doesn't exist right now so it won't be tracked by git.


.. note:: Please read the topic bellow and the instructions in local.py to continue.

.. warning:: Don't change the ``live.py``, ``dev.py`` or ``base.py`` file itself, it will cause merge conflicts when
    updating your installation.


live.py
^^^^^^^

In order to activate the ``live.py`` file you must set the environment variable ``DJANGO_IS_DEBUG`` to False. You can
do this when starting with prepending the following to your commands:

.. code-block:: bash

    $ DJANGO_IS_DEBUG=0 python manage.py runserver


dev.py
^^^^^^

The ``dev.py`` is activated without the environment variable or when the environment variable is set to 1.


base.py
^^^^^^^

The ``base.py`` is the file that combines all configurations and defines default values. It also imports and replaces data
from the ``local.py`` file.


local.py & Database
^^^^^^^^^^^^^^^^^^^

The ``local.py`` is not yet created when you clone the repository, please copy the ``local.default.py`` to ``local.py`` and
edit the contents.

More information about the configuration can be found in the :doc:`Configure Lurker <configure>` part.


Database Migrations
-------------------

Please make sure you created the schema you defined in the ``local.py`` settings file.

.. warning:: Make sure you create the database schema with collate utf-8!


To complete the installation or upgrade you must do a few tasks, first task is to run migration scripts we provided.
When installing for the first time, you must create a cache table in order to operate.

.. code-block:: bash

    $ python manage.py migrate
    $ python manage.py createcachetable

.. note:: You must be in an active `virtualenv` to execute the following statements!




Static files
------------

The static files need to be collected from all modules in order to operate on a live setup.

.. note:: This step can be ignored if you run the server under the dev configuration!


To collect static files, execute:

.. code-block:: bash

    $ python manage.py collectstatic --noinput



To compress static files, execute:

.. code-block:: bash

    $ python manage.py compress --force



Your all set to use. See the usage part on how to start and use the Mail Lurker application.
