# `in` is the intended way to test for the existence of a key in a `dict`

d = dict()
for i in xrange(105):
    key = i % 10
    if key in d:
        d[key] += 1
    else:
        d[key] = 1
print d # {0: 11, 1: 11, 2: 11, 3: 11, 4: 11, 5: 10, 6: 10, 7: 10, 8: 10, 9: 10}


dd = dict()
for i in xrange(103):
    key = i % 10
    dd[key] = dd.get(key, 0) + 1
print dd #{0: 11, 1: 11, 2: 11, 3: 10, 4: 10, 5: 10, 6: 10, 7: 10, 8: 10, 9: 10}


# ... and if you wanted to always ensure a default value for any key you can use `defaultdict` from the `collections` module, like so:

from collections import defaultdict

ddd = defaultdict(lambda: 0)
for i in xrange(106):
    ddd[i % 10] += 1
print ddd
# defaultdict(<function <lambda> at 0x10436cf50>, {0: 11, 1: 11, 2: 11, 3: 11, 4: 11, 5: 11, 6: 10, 7: 10, 8: 10, 9: 10})


dddd = {'key1': 111, 'ooo': 222}
if 'key1' in dddd:
    print 'ininini!'
else:
    print 'nonono'
# ininini!
