
a = [1, 2, 3, 1, 2, 3]
b = [3, 2, 1, 3, 2, 1]

# a & b should be considered equal, because they have exactly the same elements,
# only in different order.

# The thing is, my actual lists will consist of objects (my class instances), not integers.

############

# O(n): The Counter() method is best (if your objects are hashable):

def compare(s, t):
    return Counter(s) == Counter(t)

# O(n log n): The sorted() method is next best (if your objects are orderable):

def compare(s, t):
    return sorted(s) == sorted(t)

# O(n * n): If the objects are neither hashable, nor orderable, you can use equality:

def compare(s, t):
    t = list(t)
    try:
        for elem in s:
            t.remove(elem)
    except ValueError:
        return False
    return not t
