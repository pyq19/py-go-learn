print('append', '*' * 5)
x = [1, 2, 3]
print(x)
x.append([4, 5])
print(x)

print('extend', '*' * 5)
x = [1, 2, 3]
print(x)
x.extend([4, 5])
print(x)

# python2
# ('append', '*****')
# [1, 2, 3]
# [1, 2, 3, [4, 5]]
# ('extend', '*****')
# [1, 2, 3]
# [1, 2, 3, 4, 5]

# python3
# append *****
# [1, 2, 3]
# [1, 2, 3, [4, 5]]
# extend *****
# [1, 2, 3]
# [1, 2, 3, 4, 5]
