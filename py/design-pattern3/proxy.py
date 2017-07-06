# coding:utf8
# https://github.com/faif/python-patterns/blob/master/structural/proxy.py


from __future__ import print_function
import time


class SalesManager:
    def talk(self):
        print('sales manager ready to talk')


class Proxy:
    def __init__(self):
        self.busy = 'No'
        self.sales = None

    def talk(self):
        print('proxy checking for sales manager availability')
        if self.busy == 'No':
            self.sales = SalesManager()
            time.sleep(0.1)
            self.sales.talk()
        else:
            time.sleep(0.1)
            print('sales manager is busy')


class NoTalkProxy(Proxy):
    def talk(self):
        print('proxy checking for sales manager availability')
        time.sleep(0.1)
        print('this sales manager will not talk to you',
                'whether he/she is busy or not')


if __name__ == '__main__':
    p = Proxy()
    p.talk()
    p.busy = 'Yes'
    p.talk()
    p = NoTalkProxy()
    p.talk()
    p.busy = 'Yes'
    p.talk()

# proxy checking for sales manager availability
# sales manager ready to talk
# proxy checking for sales manager availability
# sales manager is busy
# proxy checking for sales manager availability
# this sales manager will not talk to you whether he/she is busy or not
# proxy checking for sales manager availability
# this sales manager will not talk to you whether he/she is busy or not
