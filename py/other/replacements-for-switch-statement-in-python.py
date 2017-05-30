# http://stackoverflow.com/questions/60208/replacements-for-switch-statement-in-python

def f(x):
    return {
        'a': 1,
        'b': 2,
    }[x]

def f(x):
    return {
        'a': 1,
        'b': 2,
    }.get(x, 9) # 9 is default if x not found


# result = {
#     'a': lambda x: x * 5,
#     'b': lambda x: x + 7,
#     'c': lambda x: x - 2
# }[value](x)

def f(x, v):
    return {
        'a': lambda x: x + 1,
        'b': lambda x: x + 2,
    }[x](v)
print f('a', 10) # 11
