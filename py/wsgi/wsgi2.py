#coding:utf8
#http://blog.csdn.net/on_1y/article/details/18803563

# wsgi application
# 应用程序是可调用对象
# 可调用对象有2个位置参数
# application(env, start_response)
# environ 必须包含WSGI 需要的变量(dict)
# start_response 可调用对象，接收两个位置参数,一个可选参数
# start_response(status, response_headers, exc_info=None) 
    # status 状态码 200 OK
    # response_headers 列表，列表项形式(header_name, header_value)
    # exc_info 在错误处理时使用
# start_response 必须返回一个可调用对象 write(body_data)
# 应用程序必须返回一个可迭代对象
HELLO = b'hello world!\n'
def application(environ, start_response): # callable function
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    return [HELLO]


# wsgi server
# 服务器必须将可迭代对象的内容传递给客户端， 可迭代对象会产生bytestrings，
# 必须完全完成每个bytestring 后才能请求下一个
# 假设result 为应用程序的返回的可迭代对象，如果len(result) 调用成功，那么result必须是可累积的。
# 如果result 有close 方法，那么每次完成对请求的处理时，必须调用它，无论这次请求正常完成还是错误
# 服务器程序禁止使用可迭代对象的其它属性，除非这个可迭代对象是一个特殊类的实例
# 这个类会被wsgi.file_wrapper 定义
def run(application):
    environ = {}
    
    # set environ
    def write(data):
        pass
    
    def start_response(status, response_headers, exc_info=None):
        return write

    try:
        result = application(environ, start_response)
    finally:
        if hasattr(result, 'close'):
            result.close()

    if hasattr(result, '__len__'):
        # result must be accumulated(累积的)
        pass

    for data in result:
        write(data)

####### environ 变量
#http://blog.csdn.net/on_1y/article/details/18803563
