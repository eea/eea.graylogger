""" Doc tests
"""
import doctest
import unittest
from eea.graylogger.tests.base import FUNCTIONAL_TESTING
from plone.testing import layered

OPTIONFLAGS = (doctest.REPORT_ONLY_FIRST_FAILURE |
               doctest.ELLIPSIS |
               doctest.NORMALIZE_WHITESPACE)

def test_suite():
    """ Suite
    """
    suite = unittest.TestSuite()
    suite.addTests([
        layered(
            doctest.DocFileSuite(
                'datatypes.py',
                optionflags=OPTIONFLAGS,
                package='eea.graylogger'),
            layer=FUNCTIONAL_TESTING),
    ])
    return suite
