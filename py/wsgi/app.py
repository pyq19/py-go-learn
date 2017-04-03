import re


class wsgiapp:
    def __init__(self, environ, start_response):
        self.environ = environ
        self.start = start_response
        self.status = '200 OK'
        self._headers = []

    def header(self, name, value):
        self._headers.append((name, value))

    def __iter__(self):
        x = self.delegate()
        self.start(self.status, self._headers)

        # return value can be a string or a list
        # we should be able to return an iter in both the cases.
        if isinstance(x, str):
            return iter([x])
        else:
            return iter(x)

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
        self.header('content-type', 'text/plain')
        return 'index!!!!'

    def GET_hello(self, name):  # !!!!
        self.header('content-type', 'text/plain')
        return 'hello !! -> %s' % name


    def notfound(self):
        self.header('content-type', 'text/plain')
        return 'no foound !!!'


