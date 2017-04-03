class application:
    urls = (
        ('/', 'index'),
        ('/hello', 'hello')
    )

    def __init__(self, environ, start_response):
        self.environ = environ
        self.start = start_response

    def __iter__(self):
        path_info = self.environ['PATH_INFO']
        method = self.environ['REQUEST_METHOD']
        for path, name in self.urls:
            if path == path_info:
                funcname = method.upper() + '_' + name
                func = getattr(self, funcname)
                return func()
        return self.notfound()
                
    def GET_index(self):
        status = '200 OK'
        response_headers = [('Content-type', 'text/plain')]
        self.start(status, response_headers)
        yield 'welcome!!!'

    def GET_hello(self):
        status = '200 OK'
        response_headers = [('Content-type', 'text/plain')]
        self.start(status, response_headers)
        yield 'hello!!!'

    def notfound(self):
        status = '200 OK'
        response_headers = [('Content-type', 'text/plain')]
        self.start(status, response_headers)
        yield 'notfound...!!!'


