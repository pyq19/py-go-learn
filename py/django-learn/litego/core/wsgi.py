# coding:utf8


def get_wsgi_application():
    ''' the public interface to django's WSGI support.
        should return a WSGI callable. '''
    return WSGIHandler()
#     return WSGIHandler


# def WSGIHandler(environ, start_response):
#     status = '200 OK'
#     response_headers = [('Content-type', 'text/plain')]
#     start_response(status, response_headers)
#     return ['hello world'.encode('utf-8')]


# TEMP
# from django.core.handler.wsgi import WSGIHandler TODO
class WSGIHandler(object):
    def __call__(self, environ, start_response):

        response_body = f'Request method: {environ["REQUEST_METHOD"]}'.encode('utf-8')
        # HTTP响应状态
        status = '200 OK'
        # HTTP响应头，注意格式
        response_headers = [
            ('Content-Type', 'text/plain'),
            ('Content-Length', str(len(response_body)))
        ]
        # 将响应状态和响应头交给WSGI server
        start_response(status, response_headers)
        # 返回响应正文
        return [response_body]


