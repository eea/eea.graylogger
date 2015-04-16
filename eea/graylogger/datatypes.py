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
        port = port if port else 12201
        return graypy.GELFHandler(host, port)
