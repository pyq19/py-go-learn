# coding:utf8
import litego
from litego.core.handlers.wsgi import WSGIHandler


def get_wsgi_application():
    ''' the public interface to django's WSGI support.
        should return a WSGI callable. '''
    return WSGIHandler()


