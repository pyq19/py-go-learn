# http://stackoverflow.com/questions/2600191/how-can-i-count-the-occurrences-of-a-list-item-in-python


print [1, 2, 3, 4, 1, 4, 1].count(1)


from collections import Counter
z = ['blue', 'red', 'blue', 'yellow', 'blue', 'red']
print Counter(z)
print type(Counter(z))

# 3
# Counter({'blue': 3, 'red': 2, 'yellow': 1})
# <class 'collections.Counter'>
