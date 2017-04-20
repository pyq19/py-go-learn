# Q: How do I access the index itself for a list like the following?
# ints = [8, 23, 45, 12, 78]
# When I loop through it using a `for` loop, how do I access the loop index, from 1 to 5 in this case?

# A: Using an additional state variable, such as an index variable (which you would normally use in languages such as C or PHP), is considered non-pythonic.
# The better option is to use the built-in function `enumerate()`, available in both Python 2 and 3.

ints = [8, 23, 45, 12, 78]

for idx, val in enumerate(ints):
    print(idx, val)
# (0, 8)
# (1, 23)
# (2, 45)
# (3, 12)
# (4, 78)

print ('==' * 20)
for i in range(len(ints)):
    print(i, ints[i])
# (0, 8)
# (1, 23)
# (2, 45)
# (3, 12)
# (4, 78)
