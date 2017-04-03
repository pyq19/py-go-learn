from wsgiref.simple_server import make_server

def my_app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    path = environ['PATH_INFO']
    if path == '' or path == '/':
        return 'home'
    else:
        raise NotFound

server = make_server('127.0.0.1', 8000, my_app)
server.serve_forever()
