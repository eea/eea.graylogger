""" Main product initializer
"""
from eea.graylogger.datatypes import EEAGELFHandler as GELFHandler
from eea.graylogger.datatypes import EEAGELFRabbitHandler as GELFRabbitHandler

__all__ = [
    GELFHandler.__name__,
    GELFRabbitHandler.__name__,
]
