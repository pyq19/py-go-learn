from queue import Queue
from threading import Thread

# a thread that produces data
def producer(out_q):
    while running:
        # produce some data
        data = 1
        out_q.put(data)

# a thread that consumes data
def consumer(in_q):
    while True:
        # get some data
        data = in_q.get()
        # process the data 
        data = 2
        # indicate comletion
        in_q.task_done()

# create the shared queue and launch both threads
q = Queue
t1 = Thread(target=consumer, args=(q,))
t2 = Thread(target=producer, args=(q,))
t1.start()
t2.start()

# wait for all produced items to be consumed
q.join()
