#coding:utf8

def binary_search(alist, value):
    first = 0
    last = len(alist) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last)//2
        if value == alist[midpoint]:
            found = True
        else:
            if value < alist[midpoint]:
                last = midpoint - 1
            else:
                if value > midpoint:
                    first = midpoint + 1
    return found

if binary_search([1, 2, 3, 4, 5], 2):
    print 'found !!' # found !!

# python3 
# >>> 5//2
# 2
# >>> 5/2
# 2.5
# >>> 5.0//2
# 2.0
# >>> 5.0/2
# 2.5
# >>> 5.0//3
# 1.0
# >>> 5.0/3
# 1.6666666666666667
# python 3.x里面，// 是地板除，/ 不管两边是不是整数得到的都是小数。
# >>> 3/1
# 3.0

# python2
# >>> 5//2
# 2
# >>> 5/2
# 2
# >>> 5.0//2
# 2.0
# >>> 5.0//3
# 1.0
# >>> 5.0/2
# 2.5
# >>> 5.0/3
# 1.6666666666666667
# python 2.x里面，// 是地板除，/如果有一个数是浮点数就得到小数，如果两个都是整数也是地板除。
