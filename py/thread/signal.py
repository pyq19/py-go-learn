#coding:utf8
# 用sigint代替keyboardinterrupt异常来处理用户中断

from signal import *
from time import time, sleep


def sig_handler(signum, frame):
    print 'exit'
    exit(0)

def main():
    signal(SIGINT, sig_handler)

    while True:
        sleep(1)
        print time()

if __name__ == '__main__':
    main()

# 1491658244.23
# 1491658245.23
# 1491658246.23
# 1491658247.24
# 1491658248.24
# ^Cexit


def sig_handler_pause(signum, frame):
    print 'sig ->', signum

def main_pause():
    signal(SIGUSR1, sig_handler_pause)

    while True:
        print time()
        pause()


