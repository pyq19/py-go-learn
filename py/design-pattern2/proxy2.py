# coding:utf8
# http://www.jianshu.com/p/b80e7395fd5f

class Subject(object):
    def Request(self):
        raise NotImplementedError()


class RealSubject(Subject):
    def Request(self):
        print 'real request'


class Proxy(Subject):
    def __init__(self):
        self.realSubject = RealSubject()

    def Request(self):
        self.realSubject.Request()


def client():
    proxy = Proxy()
    proxy.Request()
