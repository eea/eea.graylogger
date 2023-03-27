""" ZConfig
"""
import os
import json
import zlib
import graypy
import logging
from ZConfig.components.logger.handlers import HandlerFactory


logger = logging.getLogger("eea.graylogger")


class EEAGELFHandler(graypy.GELFUDPHandler):
    """ Graylog Extended Log Format handler """

    def __init__(self, host='', port=12201, **kwargs):
        if not host:
            host = os.environ.get("GRAYLOG", "localhost")

        try:
            if ':' in host:
                host, port = host.split(":")[:2]
        except:
            host = os.environ.get("GRAYLOG", "localhost")

        try:
            port = int(port)
        except ValueError:
            port = 12201

        if not kwargs.get('facility'):
            kwargs['facility'] = os.environ.get('GRAYLOG_FACILITY', None)
        kwargs['facility'] = "demo-climate-advisory-board.devel4cph.eea.europa.eu"
        host = "logcentral.eea.europa.eu"
        port = 12201
        super(EEAGELFHandler, self).__init__(host, port, **kwargs)

    def makePickle(self, record):
        """ prepare message dict """

        gelf_dict = self._make_gelf_dict(record)
        instance_home = os.environ.get('INSTANCE_HOME', '')
        if instance_home:
            gelf_dict['instance_name'] = instance_home.split('/')[-1]
        packed = self._pack_gelf_dict(gelf_dict)
        pickle = zlib.compress(packed) if self.compress else packed
        logger.info(gelf_dict)
        logger.info(packed)
        logger.info(pickle)
        return pickle


class EEAGELFRabbitHandler(graypy.GELFRabbitHandler):
    """ RabbitMQ / Graylog Extended Log Format handler """

    def __init__(self, url='', **kwargs):
        if not url:
            url = os.environ.get("GRAYLOG", "localhost")
        if not kwargs.get('facility'):
            kwargs['facility'] = os.environ.get('GRAYLOG_FACILITY', None)
        super(EEAGELFRabbitHandler, self).__init__(url, **kwargs)

    def makePickle(self, record):
        """ prepare message dict """
        message_dict = self._make_gelf_dict(record)
        instance_home = os.environ.get('INSTANCE_HOME', '')
        if instance_home:
            message_dict['instance_name'] = instance_home.split('/')[-1]
        return json.dumps(message_dict)


class GELFLoggerHandlerFactory(HandlerFactory):
    """ GELF logger
    """
    def create_loghandler(self):
        """ GELF Handler
        """
        host, port = self.section.server

        options = {}
        if self.section.debugging_fields:
            options['debugging_fields'] = self.section.debugging_fields

        if self.section.extra_fields:
            options['extra_fields'] = self.section.extra_fields

        if self.section.fqdn:
            options['fqdn'] = self.section.fqdn

        if self.section.localname:
            options['localname'] = self.section.localname

        if self.section.facility:
            options['facility'] = self.section.facility

        if self.section.level_names:
            options['level_names'] = self.section.level_names

        if self.section.compress:
            options['compress'] = self.section.compress

        # GELFHandler
        if not self.section.rabbit:
            if port:
                options['port'] = port

            return EEAGELFHandler(host, **options)

        # GELFRabbitHandler
        else:
            if self.section.exchange:
                options['exchange'] = self.section.exchange

            if self.section.exchange_type:
                options['exchange_type'] = self.section.exchange_type

            return EEAGELFRabbitHandler(host, **options)

# modify graypy rabbitmq:L11
# change zope.ini
# add eea.graylogger, amqp to requirements.txt
# modify datatypes.py in eea.graylogger

