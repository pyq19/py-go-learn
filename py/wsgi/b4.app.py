import re


class wsgiapp:
    def __init__(self, environ, start_response):
        self.environ = environ
        self.start = start_response

    def __iter__(self):
        return self.delegate()

    def delegate(self):
        path = self.environ['PATH_INFO']
        method = self.environ['REQUEST_METHOD']

        for pattern, name in self.urls:
            m = re.match('^' + pattern + '$', path)
            if m:
                print('**' * 20, m)
                # pass the matched groups as arguments to the function
                args = m.groups()
                funcname = method.upper() + '_' + name
                func = getattr(self, funcname)
                return func(*args) # !!!
        return self.notfound()


class application(wsgiapp):
    urls = (
        ('/', 'index'),
#        ('/hello', 'hello')
        ('/hello/(.*)', 'hello')
    )
                
    def GET_index(self):
        status = '200 OK'
        response_headers = [('Content-type', 'text/plain')]
        self.start(status, response_headers)
        yield 'welcome!!!'

    def GET_hello(self, name):  # !!!!
        status = '200 OK'
        response_headers = [('Content-type', 'text/plain')]
        self.start(status, response_headers)
        yield 'hello!!! --> %s !!!' % name

    def notfound(self):
        status = '200 OK'
        response_headers = [('Content-type', 'text/plain')]
        self.start(status, response_headers)
        yield 'notfound...!!!'


