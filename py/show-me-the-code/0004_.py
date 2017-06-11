# coding:utf8

'''
**第 0004 题：**任一个英文的纯文本文件，统计其中的单词出现的个数。
'''







####################################

from collections import Counter
import re


def create_list(filename):
    datalist = []
    with open(filename, 'r') as f:
        for line in f:
            content = re.sub('\"|,|\.', '', line)
            datalist.extend(content.strip().split(' '))
    return datalist


def wc(filename):
    print Counter(create_list(filename))

if __name__ == '__main__':
    filename = 'test.txt'
    wc(filename)




####################################
import sys


def word_count(file_path):
    file_object = open(file_path, 'r')

    word_num = 0
    for line in file_object:
        line_list = line.split()
        word_num += len(line_list)

    file_object.close()
    return word_num


# if __name__ == '__main__':
#     if len(sys.argv) <= 1:
#         print 'need at least 1 parameter. python 0004_.py text.txt'
#     else:
#         for infile in sys.argv[1:]:
#             try:
#                 print 'the total number of words is ->', word_count(infile)
#             except IOError:
#                 print 'cannot open file'
#                 pass

