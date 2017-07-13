# coding:utf8
# http://hanjianwei.com/2013/07/25/python-mro/


# >>> import inspect
# >>> class A:
#   2     def show(self):
#   3         print 'a.show()!'
# >>> class B(A):
#   2     pass
# >>> class C(A):
#   2     def show(self):
#   3         print 'c.show()!'
# >>> class D(B, C):pass
# >>> inspect.getmro(D)
# (<class ?.D at 0x10fa95f58>, <class ?.B at 0x10fc1abb0>, <class ?.A at 0x10fa9f050>, <class ?.C at 0x10fc1a940>)
# >>> x = D()
# >>> x.show()
# a.show()!

# >>> class A(object):
#   2     def show(self):
#   3         print 'A show()'
# >>> class B(A):pass
# >>> class (A):
#   2     def show(self):
#   3         print 'C show()'
# >>> class C(A):
#   2     def show(self):
#   3         print 'C show()'
# >>> class D(B, C):pass
# >>> D.__mro__
# (<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <type 'object'>)
# >>> x = D()
# >>> x.show()
# C show()

# TODO
