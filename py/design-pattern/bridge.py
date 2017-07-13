# coding:utf8
# http://dongweiming.github.io/python-bridge.html


class Bridge(object):
    
    def __init__(self):
        self.__implementation = None

    def someFunctionality(self):
        raise NotImplemented()


class UseCase1(Bridge):
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


# 这里其实才是实现的产品类
class Linux(ImplementationInterface):
    # 它定义了这个方法，回应操作系统的名字
    def anotherFunctionality(self):
        print 'linux yoooo'


class Windows(ImplementationInterface):
    
    def anotherFunctionality(self):
        print 'windows ..'


def main():
    linux = Linux()
    windows = Windows()

    useCase = UseCase1(linux)
    useCase.someFunctionality()

    useCase = UseCase1(windows)
    useCase.someFunctionality()

    useCase = UseCase2(linux)
    useCase.someFunctionality()

    useCase = UseCase2(windows)
    useCase.someFunctionality()


if __name__ == '__main__':
    main()

# UseCase1:  linux yoooo
# UseCase1:  windows ..
# UseCase2 : linux yoooo
# UseCase2 : windows ..
