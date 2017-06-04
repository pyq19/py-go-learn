# coding:utf8
# http://python.jobbole.com/87613/

import random

def get_data():
    '''返回0到9之间的3个随机数'''
    return random.sample(range(10), 3)

def consume():
    '''x显示每次传入的整数列表的动态平均值'''
    running_sum = 0
    data_items_seen = 0

    while True:
        data = yield
        data_items_seen += len(data)
        running_sum += sum(data)
        print(' the running average is {}'.format(running_sum / float(data_items_seen)))

def produce(consumer):
    '''产生序列集合，传递给消费函数 consumer '''
    while True:
        data = get_data()
        print(' produced {}'.format(data))
        consumer.send(data)
        yield

if __name__ == '__main__':
    consumer = consume()
    consumer.send(None)
    producer = produce(consumer)

    for _ in range(10):
        print('producing ...')
        next(producer)
