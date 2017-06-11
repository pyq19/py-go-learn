# coding:utf8
# http://docs.pythontab.com/interpy/decorators/deco_class/


# for-else 循环中，else 从句会在循环正常结束时候执行。
# 有个常见的构造是跑一个循环，并查找一个元素。
# 如果这个元素被找到了，我们使用break来中断这个循环。
# 有两个场景会让循环停下来。 
#   - 第一个是当一个元素被找到，break被触发。 
#   - 第二个场景是循环结束。

# 现在我们也许想知道其中哪一个，才是导致循环完成的原因。
# 一个方法是先设置一个标记，然后在循环结束时打上标记。另一个是使用else从句。

#ro  for item in container:
#     if search_something(item):
#         # Found it !
#         process(item)
#         break
# else:
#     # didn't find anything
#     not_found_in_container()


for n in xrange(2, 10):
    for x in xrange(2, n):
        if n % x == 0:
            print n, 'equals', x, '*', n/x
            break
# 4 equals 2 * 2
# 6 equals 2 * 3
# 8 equals 2 * 4
# 9 equals 3 * 3


for n in xrange(2, 10):
    for x in xrange(2, n):
        if n % x == 0:
            print n, 'equals', x, '*', n/x
            break
    else:
        # loop fell through without finding a factor
        print n, 'is a prime number'
# 2 is a prime number
# 3 is a prime number
# 4 equals 2 * 2
# 5 is a prime number
# 6 equals 2 * 3
# 7 is a prime number
# 8 equals 2 * 4
# 9 equals 3 * 3
