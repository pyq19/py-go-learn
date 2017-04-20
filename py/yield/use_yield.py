import random


def consumer():
    r = None
    while 1:
        data = yield r
        print 'consuming ->', data
        r = data + 1

def producer(consumer):
    n = 3
    consumer.send(None)
#    consumer.next()
    while n:
        data = random.choice(range(10))
        print 'produce ->', data
        rs = consumer.send(data)
        print 'consumer return ->', rs
        n -= 1
    consumer.close()

c = consumer()
producer(c)
