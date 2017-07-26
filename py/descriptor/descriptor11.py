# coding:utf8
# https://stackoverflow.com/questions/944592/best-practice-for-python-assert


class LessThanZeroException(Exception):
    pass


class variable(object):
    def __init__(self, value=0):
        # print 'get a value ->', value
        self.__x = value

    def __set__(self, obj, value):
        if value < 0:
            raise LessThanZeroException('x is less than zero')
        print 'obj.__dict__ ->', obj.__dict__
        print 'obj ->', obj

        self.__x = value

    def __get__(self, obj, objType):
        return self.__x

# obj.__dict__ -> {'variable': 123}
# obj -> <__main__.MyClass object at 0x10b793f50>
# Traceback (most recent call last):
#   File "descriptor11.py", line 39, in <module>
#     main()
#   File "descriptor11.py", line 35, in main
#     m.x -= 20
#   File "descriptor11.py", line 15, in __set__
#     raise LessThanZeroException('x is less than zero')
# __main__.LessThanZeroException: x is less than zero


class MyClass(object):
    CONSTANT = 1
    x = variable()
    def __init__(self, variable):
        self.variable = variable


def main():
    m = MyClass(123)
    m.x = 10
    m.x -= 20


if __name__ == '__main__':
    main()
