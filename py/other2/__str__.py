class Student(object):
    def __init__(self, name):
        self.name = name

print(Student('haha'))
# <__main__.Student object at 0x1019d87b8>


class Student2(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student2 object name is -> %s' % self.name

print(Student2('wawa'))
# Student2 object name is -> wawa


# >>> s = Student2('keke')
# >>> s
# <__str__.Student2 object at 0x10215bf28>


# __str__ 和 __repr__ 的区别是
# 前者返回用户看到的字符串，后者返回程序开发者看到的字符串, __repr__ 为调试服务

class Student3(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student3 object name is -> %s' % self.name

    __repr__ = __str__

# >>> s = Student3('ioio')
# >>> s
# Student3 object name is -> ioio
