# coding:utf8
# https://blog.tonyseek.com/post/notes-about-python-descriptor/


class MyDescriptor(object):
    def __get__(self, subject_instance, subject_class):
        print 'self -> %r \nsubject_instance -> %r \nsubject_class -> %r'\
        % (self, subject_instance, subject_class)
        return (self, subject_instance, subject_class)

    def __set__(self, subject_instance, value):
        print 'self -> %r \nsubject_instance -> %r \nvalue -> %r'\
        % (self, subject_instance, value)

my_descriptor = MyDescriptor()

class Spam(object):
    my = my_descriptor


spam = Spam()
spam.my = 100
# self -> <__main__.MyDescriptor object at 0x1060488d0>
# subject_instance -> <__main__.Spam object at 0x106067ed0>
# value -> 100

spam.my
# self -> <__main__.MyDescriptor object at 0x10f09e8d0>
# subject_instance -> <__main__.Spam object at 0x10f0bded0>
# subject_class -> <class '__main__.Spam'>


# Spam.my , spam.my 和 spam.my = 123 
# 都不再直接在 spam.__dict__ 上获取和添加值
# 而是调用 1. my_descriptor.__get__(None, Spam)
#          2. my_descriptor.__get__(spam, Spam)
#          3. my_descriptor.__set__(spam, 123)
# 如果MyDescriptor 实现了__delete__ 
# 那么del spam.my 也会被重载为my_descriptor.__delete__(spam)
