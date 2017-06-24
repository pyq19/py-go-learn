# coding:utf8
# http://note.axiaoxin.com/contents/borg-pattern.html


class Borg:
    __share_state = {}
    def __init__(self):
        self.__dict__ = self.__share_state


b1 = Borg()
b1.x = 100

b2 = Borg()
print b2.x

# b1.dict、b2.dict和Borg.Borgshare_state指向的是
# 同一个class attribute对象sharestate，
# 修改dict时也会修改share_state，
# 在每次初始化时都会用这个class attribute对象替换更新dict

class Singleton(object):
    def __new__(cls, *p, **k):
        if not '_the_instance' in cls.__dict__:
            cls._the_instance = object.__new__(cls)
        return cls._the_instance

s1 = Singleton()
s1.a = 100

s2 = Singleton()
print s2.a
