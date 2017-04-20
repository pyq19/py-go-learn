def a(*a):
    print a

def b(*b):
    a(b) # ((...),)
    a(*b)

t = (1, 2, 3)

b(t)
# (((1, 2, 3),),)
# ((1, 2, 3),)

b(1, 2)
# ((1, 2),)
# (1, 2)


print '--------' * 5

def a(**a):
    print a

d = dict(A=1, B='bbbbbb')
# a(d) # ERROR !
a(**d) # {'A': 1, 'B': 'bbbbbb'}

