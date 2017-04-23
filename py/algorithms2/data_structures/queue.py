'''
    Queue
    -----
    A Queue is a linear data structure, or more abstractly a sequential
    collection. The entities in the collection are kept in order and the
    principal (or only) operations on the collection are addition of
    entities to the rear terminal position, known as enqueue, and removal of
    entities from the front terminal position, know as dequeue. This makes the
    queue a Fist-In-First-Out (FIFO) data structure. In a FIFO data structure,
    the first element added to the queue will be the first one to be removed.
'''

from collections import deque

class Queue:
    def __init__(self):
        self._queue = deque([])

    def add(self, value):
        '''
        Add element as the last item in the Queue

        Worst Case Complexity: O(1)
        '''
        self._queue.append(value)

    def remove(self):
        '''
        Remove element from the front of the Queue and return it's value.

        Worst Case Complexity: O(1)
        '''
        return self._queue.popleft()

    def is_empty(self):
        '''
        Returns a boolean indicating if the Queue is empty.

        Worst Case Complexity: O(1)
        '''
        return not len(self._queue)

    def size(self):
        '''
        Return size of the Queue..

        Worst Case Complexity: O(1)
        '''
        return len(self._queue)

    def __str__(self):
        return '--> %s' % self._queue
    


if __name__ == '__main__':
    q = Queue()
    q.add(11)
    q.add('aaa')
    print q # --> deque([11, 'aaa'])
