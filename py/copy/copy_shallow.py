import copy

class MyClass:
    def __init__(self, name):
        self.name = name

    def __cmp__(self, other):
        return cmp(self.name, other.name)

a = MyClass('a')
l = [ a ]
dup = copy.copy(l)

print 'l ->', l
print 'dup ->', dup
print 'dup is l ->', (dup is l)
print 'dup == l ->', (dup == l)
print 'dup[0] is l[0] ->', (dup[0] is l[0])
print 'dup[0] == l[0] ->', (dup[0] == l[0])

# l -> [<__main__.MyClass instance at 0x10644a518>]
# dup -> [<__main__.MyClass instance at 0x10644a518>]
# dup is l -> False
# dup == l -> True
# dup[0] is l[0] -> True
# dup[0] == l[0] -> True
