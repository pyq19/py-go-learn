# coding:utf8
# http://dongweiming.github.io/python-flyweight.html


# 享元模式
# 顾名思义，共享元数据，
# 比如从文件读取很多字符串，这些字符串必定重复
# 可以使用这个模式将其存在一个pool 中


class Spam(object):
    
    def __init__(self, a, b):
        self.a = a
        self.b = b


class SpamFactory(object):
    
    def __init__(self):
        self.__instances = dict()

    def get_instance(self, a, b):
        # 在实例化后生成一个字典，当新的元组对不存在就缓存起来
        if (a, b) not in self.__instances:
            self.__instances[(a, b)] = Spam(a, b)
        return self.__instances[(a, b)]


# TODO
