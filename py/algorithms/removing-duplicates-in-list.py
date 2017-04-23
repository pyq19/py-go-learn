#coding:utf8

# Pretty much i need to write a program to check if a list has any duplicates
# and if it does it removes them and returns a new list with the items
# that weren't duplicated/removed.
# This is what i have but to be honest i do not know what to do.

def remove_duplicates():
    t = ['a', 'b', 'c', 'd']
    t2 = ['a', 'c', 'd']
    for t in t2:
        t.append(t.remove())
    return t


################
# the common approach to get a unique collection of items is to use a <set>.
# Sets are unordered collections of distinct objects.
# To create a set from any iterable, you can simply pass it to the
# built-in <set()> function.
# If you later need a real list again, you can similarly pass the set to 
# the list() function.
# the following example should cover whatever you are trying to do:

t = [1, 2, 3, 1, 2, 5, 6, 7, 8]
s = [1, 2, 3]
l = list(set(t) - set(s))

print list(set(t)) # [1, 2, 3, 5, 6, 7, 8]
print l # [8, 5, 6, 7]


###################
# the new(v2.7) Python way to remoing duplicates from an iterable while keeping it int the original order is:

from collections import OrderedDict
l = list(OrderedDict.fromkeys('asdasdaadd'))
print l # ['a', 's', 'd']

