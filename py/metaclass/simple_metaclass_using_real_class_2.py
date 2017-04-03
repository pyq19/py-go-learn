# python 2

class UpperAttrMetaclass(type):
    def __new__(upperattr_metaclass, future_class_name, future_class_parents, future_class_attr):
        uppercase_attr = {}
        for name, val in future_class_attr.items():
            if not name.startswith('__'):
                uppercase_attr[name.upper()] = val
            else:
                uppercase_attr[name] = val

        # reuse the type.__new__ method
        # this is basic OOP, nothing magic in there
        return type.__new__(upperattr_metaclass, future_class_name, future_class_parents, uppercase_attr)


# you may have noticed the extra argument `upperattr_metaclass`. 
# There is nothing special about it: __new__ always receives 
# the class it's defined in, as first parameter. 
# Just like you have `self` for ordinary methods which receive the instance as first parameter, or the defining class for class methods.

# Of course, the names I used here are long for the sake of clarity,
# but like for `self`, all the arguments have conventional names.
# So a real production metaclass would look like this:

class UpperAttrMetaclass(type):
    def __new__(cls, clsname, bases, dct):
        uppercase_attr = {}
        for name, val in dct.items():
            if not name.startswith('__'):
                uppercase_attr[name.upper()] = val
            else:
                uppercase_attr[name] = val

        return type.__new__(cls, clsname, bases, uppercase_attr)


# We can make it even cleaner by using `super`,
# which will ease inheritance (because yes, you can have metaclasses,
# inheriting from metaclasses, inheriting from type):

class UpperAttrMetaclass(type):
    def __new__(cls, clsname, bases, dct):
        uppercase_attr = {}
        for name, val in dct.items():
            if not name.startswith('__'):
                uppercase_attr[name.upper()] = val
            else:
                uppercase_attr[name] = val

        return super(UpperAttrMetaclass, cls).__new__(cls, clsname, bases, uppercase_attr)


# The reason behind the complexity of the code using metaclasses
# is not because of metaclasses, it's because you usually use metaclasses
# to do twisted stuff relying on introspection, manipulating inheritance,
# vars such as `__dict__`, etc.

# Indeed, metaclasses are especially usefull to do black magic,
# and therefore complicated stuff. But by themselves, they are simple:
#   1. intercept a class creation
#   2. modify the class
#   3. return the modified class



# Why would you use metaclasses classes instead of functions ?

# Since __metaclass__ can accept any callable, why would you use a class since it's obviously more complicated ?
# There are several reason to do so:
#   1. The intention is clear. When you read `UpperAttrMetaclass(type)`, you kow what's going to follow
#   2. You can use OOP. Metaclass can inherit from metaclass, override parent methods. Metaclass can even use metaclasses.
#   3. You can structure your code better. You never use metaclasses for something as trivial as the above example. It's usually for something complicated. Having the ability to make several methods and group them in one class is very useful to make the code easier to read.
#   4. You can hook on `__new__`, `__init__` and `__call__`.
# Which will allow you to do different stuff. Even if usually you can do it all in `__new__`, some people are just more comfortable using `__init__`.
