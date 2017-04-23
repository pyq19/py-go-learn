'''
    Stack
    -----
    A stack or LIFO (last in, first out) is an abstract data type that serves 
    as a collection of elements, with two principal operations: push, which
    adds an element to the collection, and pop, which removes the last element
    that was added.
'''

class Stack:
    def __init__(self):
        self.stack_list = []

    def add(self, value):
        '''
        Add element as last

        Time Complexity: O(1)
        '''
        self.stack_list.append(value)

    def remove(self):
        '''
        Remove element from last return value

        Time Complexity: O(1)
        '''
        return self.stack_list.pop()

    def is_empty(self):
        '''
        1 value returned on empty 0 value returned on not empty

        Time Complexity: O(1)
        '''
        return not self.size()

    def size(self):
        '''
        Return size of stack

        Time Complexity: O(1)
        '''
        return len(self.stack_list)

    def __str__(self):
        return '-->> %s' % self.stack_list

    __repr__ = __str__
        

if __name__ == '__main__':
    s = Stack()
    s.add(100)
    s.add('aasasa')
    print s # -->> [100, 'aasasa']
