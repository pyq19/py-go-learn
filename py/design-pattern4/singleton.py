# coding:utf8
# https://github.com/gennad/Design-Patterns-in-Python/blob/master/singleton.py


class Singleton(object):
    def __new__(type):
        if not '_the_instance' in type.__dict__:
            type._the_instance = object.__new__(type)
        return type._the_instance


a = Singleton()
a.toto = 12

b = Singleton()
print(b.toto)
print(id(a), id(b))


# 12
# 4339299160 4339299160


class Borg(object):
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state


a = Borg()
a.toto = 12

b = Borg()
print(b.toto)
print(id(a), id(b))


# 12
# 4331028720 4331029504  # different ! but states are sames


class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


class Borg(object):
    ''' subclassing is no problem '''
    _shared_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Borg, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_state
        return obj
