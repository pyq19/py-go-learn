

# 1
def some_function():
    for i in xrange(5):
        yield i

for i in some_function():
    print i


# 2
class It:
    def __init__(self):
        self.count = -1

    '''
    the __iter__ method will be called once by the for loop.
    the rest of the magic happens on the object returned by this method
    in this case it is the object itself
    '''
    def __iter__(self):
        return self

    def next(self):
        self.count += 1
        if self.count < 5:
            return self.count
        else:
            raise StopIteration

def some_func():
    return It()

# 2
for i in some_func():
    print i


# 2.5
iterator = some_func()
try:
    while True:
        print iterator.next()
except StopIteration:
    pass
