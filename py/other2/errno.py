#coding:utf8

import os

# os.kill(12345, 0) 
# OSError: [Errno 3] No such process
# 0表示这只是检查PID的有效性, errno 3是python内置的错误系统提供的编号


# print os.strerror(3) # No such process

import errno
def listdir(dirname):
    try:
        os.listdir(dirname)
    except OSError as e:
        error = e.errno
        if error == errno.ENOENT: # !!!
            print 'No such file or directory ...'
        elif error == errno.EACCES:
            print 'Permission denied ....'
        elif error == errno.ENOSPC:
            print 'No space left on device...'
        else:
            print e.strerror
    else:
        print 'No error !!!'

for filename in ['/no/such/dir', '/home', '/home/ubuntu']:
    listdir(filename)
# No such file or directory ...
# No error !!!
# No such file or directory ...

# 通过对比异常对象的errno属性值就能知道异常类型
