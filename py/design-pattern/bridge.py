# coding:utf8
# http://dongweiming.github.io/python-bridge.html


class Bridge(object):
    
    def __init__(self):
        self.__implementation = None

    def someFunctionality(self):
        raise NotImplemented()


class UseCasel(Bridge):
    # 根据初始化参数传入实现的产品类
    def __init__(self, implementation):
        self.__implementation = implementation
    # 根据传入的产品类的属性打印结果
    def someFunctionality(self):
        print 'UseCase1: ',
        self.__implementation.anotherFunctionality()

    
class UseCase2(Bridge):
    
    def __init__(self, implementation):
        self.__implementation = implementation

    def someFunctionality(self):
        print 'UseCase2 :',
        self.__implementation.anotherFunctionality()


class ImplementationInterface:
    
    def anotherFunctionality(self):
        raise NotImplemented


# TODO 
# 这里其实才是实现的产品类
class Linux:
    pass
