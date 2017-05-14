#coding:utf8
# http://www.jianshu.com/p/93fd09e74367

import tornado.ioloop
import tornado.web
from tornado import httpserver
from tornado.netutil import bind_unix_socket


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('hello world')

def make_app():
    return tornado.web.Application([
        (r'/', MainHandler),
    ])

if __name__ == '__main__':
    app = make_app()
    server = httpserver.HTTPServer(app, xheaders=True)
    socket = bind_unix_socket('/tmp/main_tornado.sock', mode=0o666)
    server.add_socket(socket)
    tornado.ioloop.IOLoop.current().start()

[root@localhost unix_socket]# python main.py

# # 开启另外一个窗口来访问.
# [root@localhost simple_socket]# curl --unix-socket /tmp/main_tornado.sock http://localhost/
# 
# # 显示信息
# Hello, world
