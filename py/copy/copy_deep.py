#coding:utf8

import copy

class MyClass:
    def __init__(self, name):
        self.name = name

    def __cmp__(self, other):
        return cmp(self.name, other.name)

a = MyClass('a')
l = [ a ]
dup = copy.deepcopy(l)

print 'l ->', l
print 'dup ->', dup
print 'dup is l ->', (dup is l)
print 'dup == l ->', (dup is l)
print 'dup[0] is l[0] ->', (dup[0] is l[0])
print 'dup[0] == l[0] ->', (dup[0] == l[0])

# l -> [<__main__.MyClass instance at 0x10c9e5518>]
# dup -> [<__main__.MyClass instance at 0x10c9e5560>]
# dup is l -> False
# dup == l -> False
# dup[0] is l[0] -> False
# dup[0] == l[0] -> True # !!!
