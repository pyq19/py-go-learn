#coding:utf8
# 通过一个变量 控制调用函数时 是否统计时间
# http://www.wklken.me/posts/2012/10/27/python-base-decorator.html

import logging

from time import time

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
is_debug = True

def count_time(is_debug):
    def handle_func(func):
        def handle_args(*args, **kwargs):
            if is_debug:
                begin = time()
                func(*args, **kwargs)
                logging.debug('['+func.__name__+'] ->' + str(time()))
            else:
                func(*args, **kwargs)
        return handle_args
    return handle_func

def pr():
    for i in range(1, 10000):
        i = i * 2
    print 'hello'

def test():
    pr()

@count_time(is_debug)
def test2():
    pr()

@count_time(False)
def test3():
    pr()

if __name__ == '__main__':
    test()
    test2()
    test3()

#    hello
#    hello
#    DEBUG:root:[test2] ->1494574915.03
#    hello
