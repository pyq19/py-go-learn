# coding:utf8
from wsgiref import simple_server
from litego.core.wsgi import get_wsgi_application


def get_internal_wsgi_application():
    print('in litego/core/server/basehttp.py -> get_internal_wsgi_application()')
    # from litego.conf.import settings TODO
    # app_path = getattr(settings, 'WSGI_APPLICATION')
    app_path = None
    if app_path is None:
        return get_wsgi_application()
    # try:
    #     return import_string(app_path)
    # except ImportError as e:
    #     pass


class WSGIServer(simple_server.WSGIServer, object):
    ''' BaseHTTPServer that implements the Python WSGI protocol '''
    def __init__(self, *args, **kwargs):
        if kwargs.pop('ipv6', False):
            self.address_family = socket.AF_INET6
        self.allow_reuse_address = kwargs.pop('allow_reuse_address', True)
        super(WSGIServer, self).__init__(*args, **kwargs)


class WSGIRequestHandler(simple_server.WSGIRequestHandler, object):
    pass


def run(addr, port, wsgi_handler, ipv6=False, threading=False, server_cls=WSGIServer):
    print('in litego/core/server/basehttp.py -> run()')
    server_address = (addr, port)
    if threading:
        pass
    else:
        httpd_cls = server_cls
    httpd = httpd_cls(server_address, WSGIRequestHandler, ipv6=ipv6)

    httpd.set_app(wsgi_handler)
    httpd.serve_forever()
