
def simple_app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    return ['hello world']


from werkzeug.wrappers import Response

def application(environ, start_response):
    response = Response('hello world', mimetype='text/plain')
    return response(environ, start_response)

