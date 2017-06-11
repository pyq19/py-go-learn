# coding:utf8
# https://github.com/Show-Me-the-Code/python/blob/master/AK-wang/0001/key_gen.py
# 第 0001 题：做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），
# 使用 Python 如何生成 200 个激活码（或者优惠券）？


import string
import random


KEY_LEN = 20
KEY_ALL = 200


def base_str():
    return (string.letters + string.digits)


def key_gen():
    '''生成一个激活码'''
    keylist = [random.choice(base_str()) for _ in xrange(KEY_LEN)]
    return (''.join(keylist))


def key_num(num, result=None):
    '''生成num 个激活码'''
    if result is None:
        result = []
    for i in xrange(num):
        result.append(key_gen())
    return result
    

if __name__ == '__main__':
    print key_num(5)
