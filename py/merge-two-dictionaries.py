x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 5}

# Python 3.5
# z = {**x, **y}
# print(z) {'b': 3, 'c': 5, 'a': 1}

# z = x.copy()
# z.update(y)
# print(z) {'a': 1, 'c': 5, 'b': 3}


def merge_two_dicts(x, y):
    z = x.copy()
    z.update(y)
    return z
# z = merge_two_dicts(x, y)
# print(z) # {'a': 1, 'c': 5, 'b': 3}


def merge_dicts(*dict_args):
    result = {}
    for dic in dict_args:
        result.update(dic)
    return result
a = {'g': 10, 'j': 11}
b = {'i': 12, 'o': 21}
z = merge_dicts(x, y, a, b)
print(z) # {'a': 1, 'c': 5, 'b': 3, 'g': 10, 'i': 12, 'j': 11, 'o': 21}
