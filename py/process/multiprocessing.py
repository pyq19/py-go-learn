#coding:utf8
# 3
# ERROR ---- ImportError: cannot import name Process

# from multiprocessing import Process
import os

# 子进程要执行的代码
def run_proc(name):
    print(' run child process -> %s (%s) ...' % (name, os.getpid()))

if __name__ == '__main__':
    print('parent process -> %s' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('child process will start ....')
    p.start()
    p.join() # !!!
    print('child process end...')
