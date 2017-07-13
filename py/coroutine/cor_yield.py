# coding:utf8
# http://www.jackyshen.com/2015/05/21/async-operations-in-form-of-sync-programming-with-python-yielding/

import random


def get_data():
    ''' 返回0 到9 之间的3个随机数，模拟异步操作 '''
    return random.sample(range(10), 3)


def consume():
    ''' 显示每次传入的整数列表的动态平均数 '''
    running_sum = 0
    data_items_seen = 0

    while True:
        print('Waiting to consume')
        data = yield
        data_items_seen += len(data)
        running_sum += sum(data)
        print('Consumed, the running average is {}'.format(
            running_sum / float(data_items_seen))
        )


def produce(consumer):
    ''' 产生序列集合, 传递给消费函数 (consumer) '''
    while True:
        data = get_data()
        print('Pruduced {}'.format(data))
        consumer.send(data)
        yield


if __name__ == '__main__':
    consumer = consume()
    consumer.send(None)
    producer = produce(consumer)

    for _ in range(10):
        print('Producing,,,')
        next(producer)
