# coding:utf8
# https://juejin.im/entry/59102ef661ff4b006256aa72


import time

def timer(func):
    def deco(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        stop = time.time()
        print 'stop - start =', stop - start
        return res
    return deco

@timer
def test():
    print 'test run'

# test()

# test run
# stop - start = 4.29153442383e-05


###############################3

import time

def timer(parameter):
    print parameter
    def outer_wrapper(func):
        def wrapper(*args, **kwargs):
            if parameter == 'task1':
                start = time.time()
                func(*args, **kwargs)
                end = time.time()
                print 'taks 1 end - start =', end - start
            if parameter == 'task2':
                start = time.time()
                func(*args, **kwargs)
                end = time.time()
                print 'taks 2 end - start =', end - start
            print '000'
        return wrapper
    return outer_wrapper

@timer(parameter='taks1')
def task1():
    print 'test task 1'

@timer(parameter='taks2')
def task2():
    print 'test task 2'

task1()
task2()

# taks1
# taks2
# 000
# 000
