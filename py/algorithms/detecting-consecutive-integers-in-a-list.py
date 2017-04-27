#coding:utf8

# 检测连续整数在列表中

arr = [1, 2, 3, 4, 7, 8, 10, 11, 12, 13, 14]

# I'd like to print out the ranges of consecutie integers
# 1-4, 7-8, 10-14

############

from itertools import groupby
from operator import itemgetter

data = [ 1, 4,5,6, 10, 15,16,17,18, 22, 25,26,27,28]
for k, g in groupby(enumerate(data), lambda (i, x): i-x):
    print map(itemgetter(1), g)
# [1]
# [4, 5, 6]
# [10]
# [15, 16, 17, 18]
# [22]
# [25, 26, 27, 28]
