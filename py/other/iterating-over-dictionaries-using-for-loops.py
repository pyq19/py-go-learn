d = {'x': 1, 'y': 2, 'z': 3}

# for k in d:
#     print k, 'd[k] ->', d[k]
# y d[k] -> 2
# x d[k] -> 1
# z d[k] -> 3


# loop over both key and value

# for python 2
# for k, v in d.iteritems():
#     print 'k ->', k, ' v ->', v
# k -> y  v -> 2
# k -> x  v -> 1
# k -> z  v -> 3

# for python 3
for k, v in d.items():
    print('k ->', k, ' v ->', v)
# k -> y  v -> 2
# k -> z  v -> 3
# k -> x  v -> 1
