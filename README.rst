==============
EEA Graylogger
==============
.. image:: https://ci.eionet.europa.eu/buildStatus/icon?job=eea/eea.graylogger/develop
  :target: https://ci.eionet.europa.eu/job/eea/job/eea.graylogger/job/develop/display/redirect
  :alt: develop
.. image:: https://ci.eionet.europa.eu/buildStatus/icon?job=eea/eea.graylogger/master
  :target: https://ci.eionet.europa.eu/job/eea/job/eea.graylogger/job/master/display/redirect
  :alt: master

GELF (Graylog Extended Log Format) for Zope event logs


Contents
========

.. contents::


Main features
=============

1. Sends Zope event logs to Graylog_ instead of a file.


Install
=======

Plone 5.2+ (WSGI)
-----------------

- Add `eea.graylogger`_ to your eggs section in your buildout and re-run buildout

  ::

    [instance]
    eggs +=
        eea.graylogger

    event-log-handler = eea.graylogger.GELFHandler
    event-log-args = ('logs.example.com', 12201)
    event-log-kwargs = {'level_names': True, 'facility': 'example.com'}

    access-log-handler = eea.graylogger.GELFHandler
    access-log-args = ('logs.example.com', 12201)
    access-log-kwargs = {'facility': 'example.com'}

See `graypy`_ documentation for more details.

Alternatively, you can skip `-log-args` and `-log-kwargs` and use environment variables to
define Graylog `host:port` and `facility`:

  ::

    [instance]
    eggs +=
        eea.graylogger

    event-log-handler = eea.graylogger.GELFHandler
    access-log-handler = eea.graylogger.GELFHandler

* `GRAYLOG` - Graylog `host`, or `host:port` (e.g.: `GRAYLOG=logs.example.com:12201`)
* `GRAYLOG_FACILITY` - Graylog facility (e.g.: `GRAYLOG_FACILITY=example.com`)

Plone < 5.2 (non-WSGI)
----------------------

- Add `eea.graylogger`_ to your eggs section in your buildout and re-run buildout.
  You can download a sample buildout from
  https://github.com/eea/eea.graylogger/tree/master/buildouts/plone4

  ::

    [instance]
    eggs =
        ...
        eea.graylogger

    zope-conf-imports =
      eea.graylogger

    event-log-custom =
      <graylog>
        server 172.17.0.18:12201
      </graylog>

Getting started
===============

1. Install Graylog_ server or use `Graylog2 Docker image`_
2. Restart Zope
3. Go to http://localhost:9000 to see your Zope logs

Configuration parameters
========================

* **rabbit** - True if you want to use GELFRabbitHandler instead of GELFHandler.
  See `graypy`_ documentation for more details.

GELFHandler
-----------

* **server** - the host[:port] of the graylog server.
* **debugging_fields** - send debug fields if true (the default).
* **extra_fields** - send extra fields on the log record to graylog if true (the default).
* **fqdn** - use fully qualified domain name of localhost as source host (socket.getfqdn()).
* **localname** - use specified hostname as source host.
* **facility** - replace facility with specified value. if specified, record.name
  will be passed as logger parameter.

GELFRabbitHandler
-----------------

* **server** - RabbitMQ URL (ex: amqp://guest:guest@localhost:5672/%2F).
* **exchange** - RabbitMQ exchange. Default `logging.gelf`. A queue binding must
  be defined on the server to prevent log messages from being dropped.
* **debugging_fields** - send debug fields if true (the default).
* **extra_fields** - send extra fields on the log record to graylog if true (the default).
* **fqdn** - use fully qualified domain name of localhost as source host - socket.getfqdn().
* **exchange_type** - RabbitMQ exchange type (default fanout).
* **localname** - use specified hostname as source host.
* **facility** - replace facility with specified value. if specified, record.name
  will be passed as logger parameter.


Dependencies
============

1. Graylog_ server
2. graypy_ >= 2.1.0
3. `plone.recipe.zope2instance`_ >= 6.5.0

Source code
===========

- Latest source code (Plone 5 / Python 3 compatible):
  https://github.com/eea/eea.graylogger


Copyright and license
=====================
The Initial Owner of the Original Code is European Environment Agency (EEA).
All Rights Reserved.

The EEA Graylogger (the Original Code) is free software;
you can redistribute it and/or modify it under the terms of the GNU
General Public License as published by the Free Software Foundation;
either version 2 of the License, or (at your option) any later
version.

More details under docs/License.txt


Funding
=======

EEA_ - European Environment Agency (EU)

.. _`EEA`: https://www.eea.europa.eu/
.. _`Graylog`: https://www.graylog.org
.. _`graypy`: https://pypi.org/project/graypy/
.. _`Graylog2 Docker image`: https://github.com/eea/eea.docker.graylog2
.. _`eea.graylogger`: https://github.com/eea/eea.graylogger
.. _`plone.recipe.zope2instance`: https://pypi.org/project/plone.recipe.zope2instance
