# coding:utf8
# http://python-guide-pt-br.readthedocs.io/en/latest/writing/logging/


import logging
from logging.config import fileConfig

fileConfig('logging_config.ini')
logger = logging.getLogger()
logger.debug('often makes a very good meal of %s', 'visiting tourists')


