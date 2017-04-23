#coding:utf8

# how to generate all permutations of a list in python?
# 如何在python 中生成列表的所有组合
# How do you generate all the permutations of a list in Python, independently of the type of elements in that list?
# For example:
# permutations([])
# []
# permutations([1])
# [1]
# permutations([1, 2])
# [1, 2]
# [2, 1]
# permutations([1, 2, 3])
# [1, 2, 3]
# [1, 3, 2]
# [2, 1, 3]
# [2, 3, 1]
# [3, 1, 2]
# [3, 2, 1]
# EDIT: Eliben pointed to a solution that's similar to mine although simpler, so I'm choosing it as the accepted answer, although Python 2.6+ has a builtin solution in the itertools module:
# 
# import itertools
# itertools.permutations([1, 2, 3])


###################
# Starting with Python 2.6 (and if you're on Python 3) you have a standard-library tool for this: itertools.permutations.

def all_perms(elements):
    if len(elements) <= 1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                # nb elements[0:1] works in both string and list contexts
                yield perm[:i] + elements[0:1] + perm[i:]
# A couple of alternative approaches are listed in the documentation of itertools.permutations. Here's one:

def permutations(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = range(n)
    cycles = range(n, n-r, -1)
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return

# And another, based on itertools.product:
def permutations(iterable, r=None):
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    for indices in product(range(n), repeat=r):
        if len(set(indices)) == r:
            yield tuple(pool[i] for i in indices)


###############

import itertools
itertools.permutations([1, 2, 3])
# returned as a generator. Use list(permutations(l)) to return as a list.

from itertools import permutations
arr = [9, 8, 6]
print list(permutations(arr))
# [(9, 8, 6), (9, 6, 8), (8, 9, 6), (8, 6, 9), (6, 9, 8), (6, 8, 9)]


#######
# Combination (order does NOT matter):
print list(itertools.combinations('123', 2))
# [('1', '2'), ('1', '3'), ('2', '3')]

# Cartesian product (with several iterables):
print list(itertools.product([1,2,3], [4,5,6]))
# [(1, 4), (1, 5), (1, 6), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (3, 6)]

# Cartesian product (with one iterable and itself):
print list(itertools.product([1,2], repeat=3))
# [(1, 1, 1), (1, 1, 2), (1, 2, 1), (1, 2, 2), (2, 1, 1), (2, 1, 2), (2, 2, 1), (2, 2, 2)]

#############
# http://stackoverflow.com/questions/104420/how-to-generate-all-permutations-of-a-list-in-python
