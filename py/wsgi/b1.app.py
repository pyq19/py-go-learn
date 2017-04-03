class application:
    def __init__(self, environ, start_response):
        self.environ = environ
        self.start = start_response

#     def __iter__(self):
#         status = '200 OK'
#         response_headers = [('Content-type', 'text/plain')]
#         self.start(status, response_headers)
#         yield 'hello world\n'

    def __iter__(self):
        path = self.environ['PATH_INFO']
        if path == '/':
            return self.GET_index()
        
        elif path == '/hello':
            return self.GET_hello()

        else:
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


