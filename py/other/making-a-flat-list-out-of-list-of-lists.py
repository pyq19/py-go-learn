# I wonder whether there is a shortcut to make a simple list out of list of lists in Python.
# I can do that in a for loop, but maybe there is some cool "one-liner"? I tried it with `reduce`, but I get an error.

l = [[1, 2, 3], [4, 5, 6], [7], [8, 9]]
# reduce(lambda x, y: x.extend(y), l)
# AttributeError: 'NoneType' object has no attribute 'extend'

print l

print [item for sublist in l for item in sublist]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

flatten = lambda z: [item for sublist in z for item in sublist]
print flatten(l)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]


# For evidence, as always, you can use the timeit module in the standard library:
# 
# $ python -mtimeit -s'l=[[1,2,3],[4,5,6], [7], [8,9]]*99' '[item for sublist in l for item in sublist]'
# 10000 loops, best of 3: 143 usec per loop
# $ python -mtimeit -s'l=[[1,2,3],[4,5,6], [7], [8,9]]*99' 'sum(l, [])'
# 1000 loops, best of 3: 969 usec per loop
# $ python -mtimeit -s'l=[[1,2,3],[4,5,6], [7], [8,9]]*99' 'reduce(lambda x,y: x+y,l)'
# 1000 loops, best of 3: 1.1 msec per loop




# You can use itertools.chain():
# 
# >>> import itertools
# >>> list2d = [[1,2,3],[4,5,6], [7], [8,9]]
# >>> merged = list(itertools.chain(*list2d))
# or, on Python >=2.6, use itertools.chain.from_iterable() which doesn't require unpacking the list:
# 
# >>> import itertools
# >>> list2d = [[1,2,3],[4,5,6], [7], [8,9]]
# >>> merged = list(itertools.chain.from_iterable(list2d))
# This approach is arguably more readable than [item for sublist in l for item in sublist] and appears to be faster too:
# 
# [me@home]$ python -mtimeit -s'l=[[1,2,3],[4,5,6], [7], [8,9]]*99;import itertools' 'list(itertools.chain.from_iterable(l))'
# 10000 loops, best of 3: 24.2 usec per loop
# [me@home]$ python -mtimeit -s'l=[[1,2,3],[4,5,6], [7], [8,9]]*99' '[item for sublist in l for item in sublist]'
# 10000 loops, best of 3: 45.2 usec per loop
# [me@home]$ python -mtimeit -s'l=[[1,2,3],[4,5,6], [7], [8,9]]*99' 'sum(l, [])'
# 1000 loops, best of 3: 488 usec per loop
# [me@home]$ python -mtimeit -s'l=[[1,2,3],[4,5,6], [7], [8,9]]*99' 'reduce(lambda x,y: x+y,l)'
# 1000 loops, best of 3: 522 usec per loop
# [me@home]$ python --version
# Python 2.7.3
