import unittest
import logging
import sys


class CmsTest(unittest.TestCase):
    
    def setUp(self):
        log = logging.getLogger('CmsTest.setUp')
        log.debug('set up..')

    def tearDown(self):
        log = logging.getLogger('CmsTest.tearDown')
        log.debug('tearDown')

    def testLog(self):
        log = logging.getLogger('CmsTest.testLog')
        log.debug('testLog')
    
if __name__ == '__main__':
    logging.basicConfig(stream=sys.stderr)
    logging.getLogger('CmsTest.setUp').setLevel(logging.DEBUG)
    logging.getLogger('CmsTest.tearDown').setLevel(logging.DEBUG)
    logging.getLogger('CmsTest.testLog').setLevel(logging.DEBUG)
    unittest.main()
