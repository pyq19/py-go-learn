# coding:utf8
# http://dongweiming.github.io/python-facade.html


# 外观模式
# Facade模式其实就是把一些工作接口，根据一定的组合提供一些接口，
# 比如你有1,2,3,4四种功能，你提供的接口一调用了123,接口二调用了124,接口三调用了34,这样的方式


class Test1(object):
    
    def run(self):
        print 'in test 1'


class Test2(object):
    
    def run(self):
        print 'in test 2'


class Test3(object):
    
    def run(self):
        print 'in test 3'


class Runner(object):
    
    def __init__(self):
        self.t1 = Test1()
        self.t2 = Test2()
        self.t3 = Test3()

    def build_up1(self):
        [i.run() for i in [self.t1, self.t3]]

    def build_up2(self):
        [i.run() for i in [self.t3, self.t2]]

    def build_up3(self):
        [i.run() for i in [self.t3, self.t2, self.t1]]


if __name__ == '__main__':
    run = Runner()
    # 不同的组合
    run.build_up1()
    run.build_up2()
    run.build_up3()
