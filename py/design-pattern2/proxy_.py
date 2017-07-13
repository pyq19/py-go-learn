# coding:utf8
# http://www.cnblogs.com/Xjng/p/3878839.html

from abc import ABCMeta, abstractmethod


class FemaleA():
    def __init__(self, name):
        self.name = name


class Male():
    __metaclass__ = ABCMeta

    @abstractmethod
    def send_flower(self):
        pass

    @abstractmethod
    def send_chocolate(self):
        pass

    @abstractmethod
    def send_book(self):
        pass


class MaleA(Male):
    def __init__(self, name, love_female):
        self.name = name
        self.love_female = FemaleA(love_female)

    def send_flower(self):
        print '%s send flower to %s' % (self.name, self.love_female.name)

    def send_chocolate(self):
        print '%s send chocolate to %s' % (self.name, self.love_female.name)

    def send_book(self):
        print '%s send book to %s' % (self.name, self.love_female.name)


class Proxy(Male):
    def __init__(self, name, proxyed_name, love_female):
        self.name = name
        self.proxyed = MaleA(proxyed_name, love_female)

    def send_flower(self):
        self.proxyed.send_flower()

    def send_chocolate(self):
        self.proxyed.send_chocolate()

    def send_book(self):
        self.proxyed.send_book()


if __name__ == '__main__':
    p = Proxy(u'男B', u'男A', u'女A')
    p.send_book()
    p.send_chocolate()
    p.send_flower()

# 男A send book to 女A
# 男A send chocolate to 女A
# 男A send flower to 女A


# 代理模式是一种比较常见的模式，比较典型的应用场景：
#
# RPC调用：RPC API负责代理具体的网络API调用。
# 虚拟代理：根据需要创建开销大的对象，提高性能。
# 安全代理：用来控制真实对象访问是的饿权限。
# 智能指针：当调用真实对象时，代理负责处理一些额外的工作。
