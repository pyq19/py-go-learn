# coding:utf8
# http://dongweiming.github.io/python-pototype.html


# 原型模式 Prototype


# 深拷贝，不然就是对象的引用
from copy import deepcopy


class Prototype:
    
    def __init__(self):
        self._objs = {}

    def register_object(self, name, obj):
        '''注册对象'''
        self._objs[name] = obj

    def unregister_object(self, name):
        '''取消注册'''
        del self._objs[name]

    def clone(self, name, **attr):
        '''克隆对象'''
        obj = deepcopy(self._objs[name])
        # 但是会根据attr 增加或覆盖原对象的属性
        obj.__dict__.update(attr)
        return obj


if __name__ == '__main__':
    class A:
        pass

    a = A()
    prototype = Prototype()
    prototype.register_object('a', a)
    b = prototype.clone('a', a=1, b=2, c=3)

    # 这里会返回对象a
    print a
    print b.a, b.b, b.c

# <__main__.A instance at 0x1081105f0>
# 1 2 3
