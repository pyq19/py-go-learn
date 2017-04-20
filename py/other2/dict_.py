#coding:utf8

# 根据一个或多个字典中的值来对列表排序

# 利用operator模块中的itemgetter函数对这类结构进行排序
# itemgetter() 函数还可以接收多个键，例如
# rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))
# print rows_by_lfname

rows = [
    {'fname': 'Brain', 'lname': 'John', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Clesse', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

from operator import itemgetter

rows_by_fname = sorted(rows, key=itemgetter('fname'))

rows_by_uid = sorted(rows, key=itemgetter('uid'))

# min(rows, key=itemgetter('fname'))

print(rows_by_fname)
# [
#    {'lname': 'Jones', 'uid': 1004, 'fname': 'Big'},
#    {'lname': 'John', 'uid': 1003, 'fname': 'Brain'},
#    {'lname': 'Beazley', 'uid': 1002, 'fname': 'David'},
#    {'lname': 'Clesse', 'uid': 1001, 'fname': 'John'}
# ]

print(rows_by_uid)
# [
#    {'lname': 'Clesse', 'uid': 1001, 'fname': 'John'},
#    {'lname': 'Beazley', 'uid': 1002, 'fname': 'David'},
#    {'lname': 'John', 'uid': 1003, 'fname': 'Brain'},
#    {'lname': 'Jones', 'uid': 1004, 'fname': 'Big'}
# ]


# sorted() 内建函数接收一个关键字参数key，这个参数代表一个可调用对象callable。
# callable对象从rows中(list列表)接收一个单独的元素(本例中是个dict)作为输入，
# 并返回一个用来做排序依据的值。
# itemgetter() 函数创建的就是callable对象
# operator.itemgetter()接收的参数可作为查询的标记，用来从rows的记录中提取出所需要的值。
# 它可以是字典的键名，数字表示的列元素，或是任意可以传给对象的__getitem__()方法的值。


