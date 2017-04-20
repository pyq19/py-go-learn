# error !!

from queue import Queue
from threading import Thread


# a thread that produces data
def producer(out_q):
    while True:
        # produce some data
        out_q.put(data)
        
def consumer(in_q):
    while True:
        # get some data
        data = in_q.get()
        # produce the data

# create the shared queue and launch both threads
q = Queue()
t1 = Thread(target=consumer, args=(q,))
t2 = Thread(target=producer, args=(q,))
t1.start()
t2.start()

