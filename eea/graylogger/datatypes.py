""" ZConfig
"""
import os
import json
import zlib
import graypy
from ZConfig.components.logger.handlers import HandlerFactory


class EEAGELFHandler(graypy.GELFHandler):
    """ Graylog Extended Log Format handler """

    def makePickle(self, record):
        """ prepare message dict """
        message_dict = graypy.handler.make_message_dict(
            record,
            self.debugging_fields,
            self.extra_fields,
            self.fqdn,
            self.localname,
            True,
            self.facility
        )

        instance_home = os.environ.get('INSTANCE_HOME', '')
        if instance_home:
            message_dict['instance_name'] = instance_home.split('/')[-1]

        packed = graypy.handler.message_to_pickle(message_dict)
        frame = zlib.compress(packed) if self.compress else packed
        return frame


class EEAGELFRabbitHandler(graypy.GELFRabbitHandler):
    """ RabbitMQ / Graylog Extended Log Format handler """

    def makePickle(self, record):
        """ prepare message dict """

        message_dict = graypy.handler.make_message_dict(
            record,
            self.debugging_fields,
            self.extra_fields,
            self.fqdn,
            self.localname,
            True,
            self.facility
        )

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

        # GELFHandler
        if not self.section.rabbit:
            if port:
                options['port'] = port

            if self.section.chunk_size:
                options['chunk_size'] = self.section.chunk_size

            return EEAGELFHandler(host, **options)

        # GELFRabbitHandler
        else:
            if self.section.exchange:
                options['exchange'] = self.section.exchange

            if self.section.exchange_type:
                options['exchange_type'] = self.section.exchange_type

            return EEAGELFRabbitHandler(host, **options)
