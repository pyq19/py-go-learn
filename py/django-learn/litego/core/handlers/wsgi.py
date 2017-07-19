from litego import http
from litego.core.handlers import base


class WSGIRequest(http.HttpRequest):
    def __init__(self, environ):
        script_name = get_script_name(environ)
        path_info = get_path_info(environ)
        if not path_info:
            path_info = '/'
        self.environ = environ
        self.path_info = path_info
        self.path = '%s/%s' % (script_name.rstrip('/'),
                                path_info.replace('/', '', 1))
        self.META = environ
        self.META['PATH_INFO'] = path_info
        self.META['SCRIPT_NAME'] = script_name
        self.method = environ['REQUEST_METHOD'].upper()
        self.content_type, self.content_params = cgi.parse_header(environ.get('CONTENT_TYPE', '')) # cgi
        if 'charset' in self.content_params:
            pass # TODO
        self._post_parse_error = False
        try:
            content_length = int(environ.get('CONTENT_LENGTH'))
        except:
            content_lenght = 0 # TODO
        self._stream = LimitedStream(self.environ['wsgi.input'], content_length)
        self._read_started = False
        self.resolver_match = None

    def _get_scheme(self):
        return self.environ.get('wsgi.url_scheme')

    def GET(self):
        pass

    def _get_post(self):
        pass

    def _set_post(self):
        pass

    def COOKIES(self):
        pass

    def FILES(self):
        pass

    POST = property(_get_post, _set_post)

class WSGIHandler(base.BaseHandler):
    request_class = WSGIRequest

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.load_middleware()

    def __call__(self, environ, start_response):
        # set_script_prefix(get_script_name(environ))
        # signals.request_started.send(sender=self.__class__, environ=environ)
        request = self.request_class(environ)
        response = self.get_response(request)

        response._handler_class = self.__class__

        status = '%d %s' % (response.status_code, response.reason_phrase)
        response_headers = [(str(k), str(v)) for k, v in response.items()]
        for c in response.cookies.values():
            response_headers.append((str('Set-Cookie'), str(c.output(header=''))))
        start_response(force_str(status), response_headers)
        if getattr(response, 'file_to_stream', None) is not None and environ.get('wsgi.file_wrapper'):
            response = environ['wsgi.file_wrapper'](response.file_to_stream)
        return response


def get_path_info(environ):
    ''' return the HTTP request's PATH_INFO as a unicode string '''
    path_info = get_bytes_from_wsgi(environ, 'PATH_INFO', '/')
    # return repercent_broken_unicode(path_info).decode(UTF_8)
    return None
