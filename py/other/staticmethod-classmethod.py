#coding:utf8

# The difference between a function decorated with `@staticmethod` and one decorated with `@classmethod`

# Maybe a bit of example code will hell:
# Notice the difference in the call signatures of `foo`, `class_foo` and `static_foo`:

class A(object):
    def foo(self, x):
        print 'executing foo(%s, %s)' % (self, x)

    @classmethod
    def class_foo(cls, x):
        print 'executing class_foo(%s, %s)' % (cls, x)

    @staticmethod
    def static_foo(x):
        print 'executing static_foo(%s)' % x

a = A()

a.foo(1) # executing foo(<__main__.A object at 0x105fab150>, 1)

a.class_foo(1) # executing class_foo(<class '__main__.A'>, 1)

a.static_foo(1)
A.static_foo('hi')
# executing static_foo(1)
# executing static_foo(hi)

# `foo` is just a function, but when you call `a.foo` you don't just get the function, you get a "partially applied" version of the function with the object instance `a` bound as the first argument to the function. `foo` expects 2 arguments, while `a.foo` only expects 1 argument.

# `a` is bound to `foo`. That is what meant by the term "bound“ below.
print(a.foo) # <bound method A.foo of <__main__.A object at 0x10de5c150>>

# With `a.class_foo`, `a` is not bound to `class_foo`, rather the class `A` is bound to `class_foo`.
print(a.class_foo) # <bound method type.class_foo of <class '__main__.A'>>

# Here, with a staticmethod, even though it is a method, `a.static_foo` just returns a function with no argument bound. `static_foo` expects 1 argument, and `a.static_foo` expects 1 argument too.
print(a.static_foo) # <function static_foo at 0x107f27a28>

# And of course the same thing happens when you call `static_foo` with the class `A` instead.
print(A.static_foo) # <function static_foo at 0x10e333a28>


# Basically `@classmethod` makes a method whose first argument is the class it's called from (rather than the class instance), `@staticmethod` does not have any implicit arguments.
