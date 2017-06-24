# coding:utf8
# http://dongweiming.github.io/python-borg.html


# Borg 模式


class Config(object):
    
    _we_are_one = {}
    _myvalue = ''

    def __new__(cls, *p, **k):
        self = object.__new__(cls, *p, **k)
        self.__dict__ = cls._we_are_one
        return self

    def myvalue(self, value=None):
        if value:
            self._myvalue = value
        return self._myvalue


if __name__ == '__main__':
    conf = Config()
    conf.myvalue('hello')
    conf2 = Config()
    print conf2.myvalue()

# 在修改myvalue的时候不仅修改了conf.__dict__
# 还修改了Config._we_are_one


def borg(cls):
    cls._state = {}
    orig_init = cls.__init__
    def new_init(self, *args, **kwargs):
        self.__dict__ = cls._state
        orig_init(self, *args, **kwargs)
    cls.__init__ = new_init
    return cls


@borg
class TestBorg(object):
    def say_borg(self):
        print ' i am borg'

