# coding:utf8
# http://blog.thedigitalcatonline.com/blog/2015/01/12/accessing-attributes-in-python/

# what are attributes
class Book: # new style class python 3, in 2 class Book(object):
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def get_entry(self):
        return '{0} by {1}'.format(self.title, self.author)

# Basic attribute access
b = Book(title='Pawn of Prophecy', author='David Eddings')
print(b.title) # Pawn of Prophecy
print(b.get_entry) # <bound method Book.get_entry of <__main__.Book instance at 0x1013fc050>>

# python objects provide a wide range of automatically created
# attributes such as __class__ or __doc__
print(b.__class__) # __main__.Book


# Properties
class Book(object):
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def get_entry(self):
        return '{0} by {1}'.format(self.title, self.author)
    entry = property(get_entry)
# The above syntax defines an entry attribute which automatically calls self.get_entry() when read.
b = Book(title='Pawn of Prophecy', author='David Eddings')
print(b.entry) # Pawn of Prophecy by David Eddings

# properties allow to specify also a write method (a setter),
# that is automatically called when you try to change the 
# value of the property itself.
class Book(object):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def _get_entry(self):
        return '{0} by {1}'.format(self.title, self.author)

    def _set_entry(self, value):
        if ' by ' not in value:
            raise ValueError('entries shall be formatted as <title> by <author>')
        self.title, self.author = value.split(' by ')
    
    entry = property(_get_entry, _set_entry)
b = Book(title='Pawn of Prophecy', author='David Eddings')
print(b.entry)
b.entry = 'hello by Mccree'
print(b.entry)
# b.entry = 'asd' # ValueError: entries shall be formatted as <title> by <author>

# properties are part of the class itself.
# print(Book.title) # AttributeError: type object 'Book' has no attribute 'title'
print(Book.entry) # <property object at 0x1011a74a8>


# Softcoding attribute access
print(getattr(b, 'title')) # hello
print(getattr(b, '_get_entry'))
# <bound method Book._get_entry of <__main__.Book object at 0x1018a0940>>

for attr in ['title', 'author']:
    print(getattr(b, attr))
# hello
# Mccree


# Avoiding to fail
# dotted syntax or with `getattr()` to access an attribute
# that does not exit, use `__getattr__()` before raise 
# `AttributeError`.
class Book(object):
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def get_entry(self):
        return '{0} by {1}'.format(self.title, self.author)
    def __getattr__(self, attr):
        return 'None...'
b = Book(title='LLL', author='MCCREE')
print(b.title)      # LLL
print(b.not_exist)  # None...


