from litego.conf import settings
from litego.urls import set_urlconf
from .exception import (
    convert_exception_to_response,
)



class BaseHandler(object):
    def __init__(self):
        self._request_middleware = None
        self._view_middleware = None
        self._template_response_middleware = None
        self._response_middleware = None
        self._exception_middleware = None
        self._middleware_chain = None

    def load_middleware(self):
        self._request_middleware = []
        self._view_middleware = []
        self._template_response_middleware = []
        self._response_middleware = []
        self._exception_middleware = []

        if settings.MIDDLEWARE is None:
            handler = convert_exception_to_response(self._legacy_get_response)
        else:
            handler = None # TODO


        self._middleware_chain = handler

    def make_view_atomic(self, view):
        pass

    def get_exception_response(self, request, resolver, status_code, exception):
        pass

    def get_response(self, request):
        ''' return an HttpResponse object for the given HttpRequest '''
        set_urlconf(settings.ROOT_URLCONF)
        response = self._middleware_chain(request)

        # if MIDDLEWARE is used, self._response_middleware will be empty
        try:
            for middleware_method in self._response_middleware:
                response = middleware_method(request, response)
                if response is None:
                    raise ValueError(
                        "%s.process_response didn't return an"
                        "HttpRespone object. It returned None instead"
                        % (middleware_method.__self__.__class__.__name__))
        except Exception:
            pass # TODO

    def _get_response(self, request):
        pass

    def process_exception_by_middleware(self, exception, request):
        pass

    def handle_uncaught_exception(self, request, resolver, exc_info):
        pass

    def _legacy_get_response(self, request):
        pass
