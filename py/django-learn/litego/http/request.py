from litego.utils.datastructures import MutiValueDict


class HttpRequest(object):
    ''' a basic HTTP request. '''

    _encoding = None
    _upload_handlers = []

    def __init__(self):
        self.GET = QueryDict(mutable=True)
        self.POST = QueryDict(mutable=True)
        self.COOKIES = {}
        self.META = {}
        self.FILES = MultiValueDict()

        self.path = ''
        self.path_info = ''
        self.method = None
        self.resolver_match = None
        self._post_parse_error = False
        self.content_type = None
        self.content_params = None


class QueryDict(object):
    pass
