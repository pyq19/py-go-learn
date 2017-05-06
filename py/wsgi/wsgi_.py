#coding:utf8

# WSGI 规定
# 1. 应用程序是一个可调用对象，接收两个参数

# 如果这个对象是函数
# callable function
def application(environ, start_response):
    pass

# 如果这个对象是类
# callable class
class Application:
    def __init__(self, environ, start_response):
        pass

# 如果这个对象是类的实例
# callable object
class ApplicationObj:
    def __call__(self, environ, start_response):
        pass

# 2. 可调用对象返回一个值，这个值是可迭代的
HELLO_WORLD = b'hello world!\n'
def application(environ, start_response):
    return [HELLO_WORLD]

class Application:
    def __init__(self, environ, start_response):
        pass
    def __iter__(self):
        yield HELLO_WORLD

class ApplicationObj:
    def __call__(self, environ, start_response):
        return [HELLO_WORLD]


# 3. 服务器程序需要调用应用程序
def run(application):
    # 把应用程序需要的两个参数设置好
    environ = {}
    def start_response(status, response_headers, exc_info=None):
        pass

    # 调用应用程序
    result = application(environ, start_response)

    # 迭代访问应用程序的返回结果，并将其传回客户端
    def write(data):
        pass
    def data in result:
        write(data)


# middleware (中间件)
# e.g. URL Routing middleware
def urlrouting(url_app_mapping):
    def midware_app(environ, start_response):
        url = environ['PATH_INFO']
        app = url_app_mapping[url]
        result = app(environ, start_response)
        return result
    return midware_app
# 对服务器它是一个应用程序，是一个可调用对象，有2个参数，返回一个可调用对象。
# 对应用程序，它是一个服务器，为应用程序提供参数，并调用应用程序
# urlrouting 相当于函数生成器，给不同的url-app 映射关系，生成相应的具有url routing 功能的middleware.

