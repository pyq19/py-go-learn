
import threading

# worker thread
def worker(n, sema):
    # wait to be signaled
    sema.acquire()
    # do some work
    print('working ->', n)

# create some thread
sema = threading.Semaphore(0)
nworkers = 10
for n in range(nworkers):
    t = threading.Thread(target=worker, args=(n, sema,))
    t.start()

sema.release() # working -> 0

sema.release() # working -> 1
