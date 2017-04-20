from queue import Queue
from threading import Thread

# object that signals shutdown
_sentinal = object()

# a thread that produces data
def producer(out_q):
    while running:
        # produce some data
        # data = 111
        out_q.put(data)

    # put the sentinel on the queue to indicate completion
    out_q.put(_sentinel)

# a thread that consumes data
def consumer(in_q):
    while True:
        # get some data
        data = in_q.get()

        # check for termination
        if data is _sentinel:
            in_q.put(_sentinel)
            break

        # process the data
        print(data)

