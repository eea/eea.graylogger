==============
EEA Graylogger
==============
.. image:: http://ci.eionet.europa.eu/job/eea.graylogger-www/badge/icon
  :target: http://ci.eionet.europa.eu/job/eea.graylogger-www/lastBuild
.. image:: http://ci.eionet.europa.eu/job/eea.graylogger-plone4/badge/icon
  :target: http://ci.eionet.europa.eu/job/eea.graylogger-plone4/lastBuild

GELF (Graylog Extended Log Format) for Zope event logs


Contents
========

.. contents::


Main features
=============

1. Sends Zope event logs to Graylog_ instead of a file.


Install
=======

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
* **chunk_size** - message chunk size. messages larger than this size will be sent
  to graylog in multiple chunks (default 1420).
* **debugging_fields** - send debug fields if true (the default).
* **extra_fields** - send extra fields on the log record to graylog if true (the default).
* **fqdn** - use fully qualified domain name of localhost as source host (socket.getfqdn()).
* **localname** - use specified hostname as source host.
* **facility** - replace facility with specified value. if specified, record.name
  will be passed as logger parameter.

GELFRabbitHandler
-----------------

* **server** - RabbitMQ URL (ex: amqp://guest:guest@localhost:5672/%2F).
* **exchange** - RabbitMQ exchange. Default ‘logging.gelf’. A queue binding must
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
2. graypy_

Source code
===========

- Latest source code (Plone 4 compatible):
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

.. _`EEA`: http://www.eea.europa.eu/
.. _`Graylog`: https://www.graylog.org
.. _`graypy`: https://pypi.python.org/pypi/graypy
.. _`Graylog2 Docker image`: https://github.com/eea/eea.docker.graylog2
.. _`eea.graylogger`: https://github.com/eea/eea.graylogger
