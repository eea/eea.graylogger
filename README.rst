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

The EEA Progress Bar (the Original Code) is free software;
you can redistribute it and/or modify it under the terms of the GNU
General Public License as published by the Free Software Foundation;
either version 2 of the License, or (at your option) any later
version.

More details under docs/License.txt


Funding
=======

EEA_ - European Environment Agency (EU)

.. _EEA: http://www.eea.europa.eu/
.. _Graylog: https://www.graylog.org
.. _graypy: https://pypi.python.org/pypi/graypy
.. _`Graylog2 Docker image`: https://github.com/eea/eea.docker.graylog2
