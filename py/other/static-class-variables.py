#coding:utf8

# 静态类变量
# static class variables in Python

# Is it possible to have static class variables or methods in python?
# What syntax is required to do this?

################

# Variables declared inside the class definition,
# but not inside a method are class or static variables:

class MyClass:
    i = 3
print MyClass.i # 3

# This creates a class-level "i" variable,
# but this is distinct from any instance-level "i" variable,
# so you could have:

m = MyClass()
m.i = 4
print 'MyClass.i ->', MyClass.i # MyClass.i -> 3
print 'm.i ->', m.i # m.i -> 4

# http://stackoverflow.com/questions/68645/static-class-variables-in-python
