import threading
from contextlib import contextmanager


# thread-local state to stored information on locks already acquired
_local = threading.local()

@contextmanager
def acquired(*locks):
    # sort locks by object identifier
    locks = sorted(locks, key=lambda x: id(x))

    # make sure lock order of previously acquired locks is not violated
    acquired = getattr(_local, 'acquired', [])
    if acquired and max(id(lock) for lock in acquired) >= id(locks[0]):
        raise RuntimeError('Lock Order Violation')

    # acquire all of the locks
    acquired.extend(locks)
    _local.acquired = acquired
    try:
        for lock in locks:
            lock.acquire()
        yield
    finally:
        # release locks in reverse order of acquisition
        for lock in reversed(locks):
            lock.release()
        del acquired[-len(locks):]
