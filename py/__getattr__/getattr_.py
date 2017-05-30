# coding:utf8
# http://luozhaoyu.iteye.com/blog/1506426

class C(object):
    a = 'ABC'
    
    def __getattribute__(self, *args, **kwargs):
        print('__getattribute__() is called')
        return object.__getattribute__(self, *args, **kwargs)

    def __getattr__(self, name):
        print('__getattr__() is called')
        return name + ' <- from getattr'

    def __get__(self, instance, owner):
        print('__get__() is called', instance, owner)
        return self

    def foo(self, x):
        print(x)

class C2(object):
    d = C()

if __name__ == '__main__':
    c = C()
    c2 = C2()
    print('='*20)           # 1
    print(c.a)
    print('='*20)           # 2
    print(c.zzz)
    print('='*20)           # 3
    c2.d
    print('='*20)           # 4
    print(c2.d.a)
    print('='*20)           # 5

# ====================          # 1
# __getattribute__() is called
# ABC
# ====================          # 2
# __getattribute__() is called
# __getattr__() is called
# zzz <- from getattr
# ====================          # 3
# __get__() is called <__main__.C2 object at 0x101985978> <class '__main__.C2'>
# ====================          # 4
# __get__() is called <__main__.C2 object at 0x101985978> <class '__main__.C2'>
# __getattribute__() is called
# ABC
# ====================          # 5
