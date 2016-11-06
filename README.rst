Mail Lurker
===========

.. image:: https://travis-ci.org/tomvlk/maillurker.svg?branch=master
        :target: https://travis-ci.org/tomvlk/maillurker

.. image:: https://coveralls.io/repos/github/tomvlk/maillurker/badge.svg?branch=master
        :target: https://coveralls.io/github/tomvlk/maillurker?branch=master


A ordered and structured mail catcher made for large environments with high e-mail traffic from multiple sources.
With the global level filtering and user defined filtering it's easy to maintain structure in debugging with multiple
developers and servers.

* Documentation: https://tomvlk.github.io/maillurker/
* GitHib: https://github.com/tomvlk/maillurker/
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

* Social Authentication: Allows your users to authenticate with social authentication. This can be really useful when
  your company uses Google for Domains, you can easily allow the specific domain to be allowed.

* REST Api: Allows you and (optional) your users to create awesome integrations for creating filters, rules and reading
  several data from the lurker.

Similar projects
----------------

* MailCatcher (Ruby): https://github.com/sj26/mailcatcher
* MailHog (Go): https://github.com/mailhog/MailHog
* MailDev (JavaScript): https://github.com/djfarrelly/MailDev


Requirements
------------

The Mail Lurker requires the following software components:

-  Linux or MacOS
-  Python 3.4+
-  pip
-  virtualenv
-  MySQL (Or any other database supported by Django).
