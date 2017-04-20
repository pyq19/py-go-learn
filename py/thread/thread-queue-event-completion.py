from queue import Queue
from threading import Thread, Event


# a thread that produces data
def producer(out_q):
    while running:
        # produce some data
        data = 1
        # make an (data, event) pair and hand it to the consumer
        evt = Event()
        out_q.put((data, evt))
        # ...
        # wait for the consumer to process the items
        evt.wait()

# a thread that consumes data
def consumer(in_q):
    while True:
        # get some data
        data, evt = in_q.get()
        # process the data
        data = '...'
        # indecate completion
        evt.set()

