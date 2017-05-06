#coding:utf8

# http://blog.csdn.net/sraing/article/details/8455242

# wsgi 是一个web 组件的接口规范，wsgi 将web 组件分为3类：
# web 服务器， web 中间件， web 应用程序
# wsgi 基本处理模式: WSGI Server -> (WSGI Middleware) -> WSGI Application

# WSGI Server/Gateway
# wsgi server 接收request 请求, 封装一系列环境变量, 按照wsgi 规范调用
# 注册的wsgi app, 最后将response 返回给客户端.
# 工作流程:
# 1. 服务器创建socket，监听端口，等待客户端连接。
# 2. 当有请求来时，服务器解析客户端信息放到环境变量environ 中，并调用绑定的handler处理请求。
# 3. handler 解析这个http 请求，将请求信息（例如method，path等）放到environ 中。
# 4. wsgi handler 再将一些服务器端信息也放到environ 中，最后服务器信息，客户端信息，本次请求信息全部都保存到环境变量environ 中。
# 5. wsgi handler 调用注册的wsgi app，并将environ 和回调函数传给wsgi app。
# 6. wsgi app 将response header/status/body 回传给wsgi handler。
# 7. 最终handler 还是通过socket 将response 信息塞回给客户端。

# WSGI Application
# wsgi app 就是一个普通的callable 对象，当有请求到来时，wsgi server会调用这个wsgi app.
# 这个对象接收两个参数，通常为environ, start_response. environ 如前所述可以理解为环境变量，跟一次请求相关的所有信息都保存在环境变量中，包括服务器信息，客户端信息，请求信息。
# start_response 是一个callback 函数，wsgi application 通过调用start_response，将
# response headers/status 返回给wsgi server. 此外wsgi app 会返回iterator 对象，
# 这个iterator 就是response body.
# def simple_app(environ, start_response):
#     status = '200 OK'
#     response_headers = [('Content-type', 'text/plain')]
#     start_response(status, response_headers)
#     return [u'hello'.encode('utf8')]
# 
# from wsgiref.simple_server import make_server
# httpd = make_server('', 8000, simple_app)
# httpd.serve_forever()

# class AppClass:
#     def __call__(self, environ, start_response):
#         status = '200 OK'
#         response_headers = [('Content-type', 'text/plain')]
#         start_response(status, response_headers)
#         return ['hello']
# app = AppClass()
# from wsgiref.simple_server import make_server
# httpd = make_server('', 8000, app)
# httpd.serve_forever()

# WSGI MiddleWare
URL_PATTERNS = (
    ('hi/', 'say_hi'),
    ('hello/', 'say_hello'),
)

class Dispatcher(object):
    def _match(self, path):
        path = path.split('/')[1]
        print path
        for url, app in URL_PATTERNS:
            if path in url:
                return app

    def __call__(self, environ, start_response):
        path = environ.get('PATH_INFO', '/')
        app = self._match(path)
        if app:
            app = globals()[app] # !!!
            return app(environ, start_response)
        else:
            start_response('400 NOT FOUND', [('Content-type', 'text/plain')])
            return ['page not found..']

def say_hi(environ, start_response):
    start_response('200 OK', [('Content-type', 'text/html')])
    return ['say hi..']

def say_hello(environ, start_response):
    start_response('200 OK', [('Content-type', 'text/html')])
    return ['say hello..']

app = Dispatcher()
from wsgiref.simple_server import make_server
httpd = make_server('', 8000, app)
httpd.serve_forever()

# wsgi middleware  auth
# class Auth(object):
#     def __init__(self, app):
#         self.app = app
#     
#     def __call__(self, environ, start_response):
#         # todo 
#         return self.app(environ, start_response)
# app = Dispatcher()
# auth_app = Auth(app)
# httpd = make_server('', 8000, auth_app)
# httpd.serve_forever()

# def configure(app):
#     return ErrorHandlerMiddleware(
#             SessionMiddleware(
#              IdentifiecationMiddleware(
#               AuthenticationMiddleware(
#                UrlParserMiddleware(app)))))
