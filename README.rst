Email Lurker
============

.. image:: https://travis-ci.org/tomvlk/emaillurker.svg?branch=master
        :target: https://travis-ci.org/tomvlk/emaillurker

.. image:: https://codecov.io/gh/tomvlk/emaillurker/branch/master/graph/badge.svg
        :target: https://codecov.io/gh/tomvlk/emaillurker


A ordered and structured mail catcher made for large environments with high e-mail traffic from multiple sources.
With the global level filtering and user defined filtering it's easy to maintain structure in debugging with multiple
developers and servers.

* Documentation: https://tomvlk.github.io/emaillurker/
* GitHib: https://github.com/tomvlk/emaillurker/
* License: Open Source, LGPL 3.0


Features
--------

* Catch and debug in realtime: Real-time updates when messages are being received by the server.

* SMTP Server: Includes a basic SMTP server to catch all messages on. The SMTP Server runs in a different process as the
  webserver does.

* Filter sets: You can setup global filter sets that can be used by all users. And all users can create their own
  personal filter sets.

* Filtering with rules: Filter sets have multiple rules that can be fully customized. Rules apply on different fields
  of the e-mail messages.

* User system: You can optional enable the authentication required command in the settings. This will require an
  authenticated user in order to use the catcher.



Similar projects
----------------

* MailCatcher (Ruby): https://github.com/sj26/mailcatcher
* MailHog (Go): https://github.com/mailhog/MailHog
* MailDev (JavaScript): https://github.com/djfarrelly/MailDev


Requirements
------------

The Email Lurker requires the following software components:

-  Linux or MacOS
-  Python 3.4+
-  pip
-  virtualenv
-  MySQL (for now, only MySQL is supported).