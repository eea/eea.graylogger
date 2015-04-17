""" ZConfig
"""
import graypy
from ZConfig.components.logger.handlers import HandlerFactory

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

            return graypy.GELFHandler(host, **options)

        # GELFRabbitHandler
        else:
            if self.section.exchange:
                options['exchange'] = self.section.exchange

            if self.section.exchange_type:
                options['exchange_type'] = self.section.exchange_type

            return graypy.GELFRabbitHandler(host, **options)
