# run on Python 2

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return '<h1>hello world</h1>'

from wsgiref.simple_server import make_server

httpd = make_server('', 8000, application)

httpd.serve_forever()
