# coding:utf8
# https://github.com/faif/python-patterns/blob/master/creational/lazy_evaluation.py


from __future__ import print_function
import functools


class lazy_property(object):
    def __init__(self, function):
        self.function = function
        functools.update_wrapper(self, function)

    def __get__(self, obj, type_):
        if obj is None:
            return self
        val = self.function(obj)
        obj.__dict__[self.function.__name__] = val
        return val


class Person(object):
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation

    @lazy_property
    def relatives(self):
        # Get all relatices, let's assume that it costs much time.
        relatives = 'Many relatives'
        return relatives


def main():
    John = Person('John', 'Coder')
    print('Name: {0} Occupation: {1}'.format(John.name, John.occupation))
    print('before we access `relatives`:')
    print(John.__dict__)
    print(f'Jhon s relatives: {John.relatives}')
    # print('Jhon s relatives: {0}'.format(John.relatives))
    print('After we ve access `relatives`:')
    print(John.__dict__)


if __name__ == '__main__':
    main()

# Name: John Occupation: Coder
# before we access `relatives`:
# {'name': 'John', 'occupation': 'Coder'}
# Jhon s relatives: Many relatives
# After we ve access `relatives`:
# {'name': 'John', 'occupation': 'Coder', 'relatives': 'Many relatives'}
