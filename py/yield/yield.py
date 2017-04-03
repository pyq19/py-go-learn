from contextlib import contextmanager
from collections import defaultdict


class Exchange:
    def __init__(self):
        self._subscribers = set()

    def attach(self, task):
        self._subscribers.add(task)

    def detach(self, task):
        self._subscribers.remove(task)


@contextmanager
def subscribe(self, *tasks):
    for task in tasks:
        self.attach(task)
    try:
        yield
    finally:
        for task in tasks:
            self.detach(task)

    def send(self, msg):
        for subscriber in self._subscribers:
            subscriber.send(msg)


# dictionary of all created exchanges
_exchanges = defaultdict(Exchange)

# return the exchange instance associated with a given name
def get_exchange(name):
    return _exchanges[name]

# example of using the subscribe() method
exc = get_exchange('name')
with exc.subscribe(task_a, task_b):
    '''
    exc.send('msg1')
    exc.send('msg2')
    '''

# task_a and task_b detached here
