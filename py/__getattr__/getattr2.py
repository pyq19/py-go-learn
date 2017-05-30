# coding:utf8
# http://www.goliatone.com/blog/2013/10/06/python-get-vs-getattr-vs-getattribute/

# __getattr__ is [only] invoked if the attribute is not defined
# in the instance and it was not found.

# __getattribute__ is invoked before looking for the attribute
# in the object instance. It has precedence over __getattr__


# Descriptors(描述符)
# descriptors allow us to intercept(拦截) an instance's
# get/set/delete calls.

# if you want to make the attribute read only,
# you should implement __set__ and just pass.
class Descriptor(object):
    def __get__(self, instance, owner):
        return instance._name
    def __set__(self, instance, value):
        instance._name = ' '.join([e.capitalize() for e in value.split()])

class Person(object):
    name = Descriptor()


# Getters and setters: decorators
class Person(object):
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = ' '.join([e.capitalize() for e in name.split()])

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age


# Properties
# we could also use the builtin property function.
# attribute = property(get, set, del, doc)
class Person(object):
    def setName(self, name):
        self._name = ' '.join([e.capitalize() for e in name.split()])
    def getName(self):
        return self._name
    name = property(getName, setName)

