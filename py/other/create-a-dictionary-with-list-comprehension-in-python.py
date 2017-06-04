# https://stackoverflow.com/questions/1747817/create-a-dictionary-with-list-comprehension-in-python

d = dict((key, value) for (key, value) in iterable)

d = {key: value for (key, value) in iterable}

d = {value: foo(value) for value in sequence if bar(value)}

def key_value_gen(k):
    yield chr(k+65)
    yield chr((k+13)%26+65)
d = dict(map(key_value_gen, range(26)))

d = {k: v for k, v in iterable}

ts = [(1, 2), (3, 4), (5, 6)]
dict(ts)
# {1: 2, 3: 4, 5: 6}

list1, list2 = ['a', 'b', 'c'], [1, 2, 3]
dict(zip(list1, list2))
# {'a': 1, 'c': 3, 'b': 2}
