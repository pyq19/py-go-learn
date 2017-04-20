#coding:utf8

# 不明白

from os import getpid
from time import sleep
from signal import signal, SIGTERM
from multiprocessing import Process

def test():
    def handler(signum, frame):
        print 'child exit. ->', getpid()
        exit(0)
    signal(SIGTERM, handler)
    print 'child start ->', getpid()
    while True: sleep(1)


if __name__ == '__main__':
    p = Process(target=test)
    p.deamon = True
    p.start()

    sleep(2)
    print 'parent exit.'
