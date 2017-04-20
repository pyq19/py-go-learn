from compiler.ast import flatten

d = flatten([1, [2], [3, [4]]]) # [1, 2, 3, 4]

print d

