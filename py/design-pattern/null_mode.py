# coding:utf8
# http://dongweiming.github.io/python-null.html


class A(object):
    pass


class B(object):
    b = 1
    @classmethod
    def test(cls):
        print cls.b


def get_test(x):
    try:
        return x.test
    except AttributeError:
        return None


for i in [A, B]:
    test = get_test(i)
    # 判断以下是否获得这个类方法才能决定是否可以执行
    if test:
        test()


class Null(object):
    
    def __init__(self, *args, **kwargs):
        '''忽略参数'''
        return None

    def __call__(self, *args, **kwargs):
        '''忽略实例调用'''
        return self

    def __getattr__(self, mname):
        '''忽略属性获得'''
        return self

    def __setattr__(self, name, value):
        '''忽略设置属性操作'''
        return self

    def __delattr__(self, name):    
        '''忽略删除属性操作'''
        return self

    def __repr__(self):
        return '<Null>'

    def __str__(self):
        return 'null.'


def get_test_with_null(x):
    try:
        return x.text
    # 异常处理返回Null 类
    except AttributeError:
        return Null()


for i in [A, B]:
    # 直接调用不需要判断
    get_test_with_null(i)()
