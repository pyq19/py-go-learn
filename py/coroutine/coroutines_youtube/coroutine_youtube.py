# coding:utf8
# https://www.youtube.com/watch?v=7sCu4gEjH5I&list=PLTOBJKrkhpoMdsT9RUERSDdEVrViykAEQ&index=1



from selectors import DefaultSelector, EVENT_WRITE, EVENT_READ
import socket
import time

selector = DefaultSelector()
n_tasks = 0


class Future(object):
    def __init__(self):
        self.callbacks = []

    def resolve(self):
        for c in self.callbacks:
            c()


def get(path):
    global n_tasks
    n_tasks += 1
    s = socket.socket()
    s.setblocking(False)
    try:
        s.connect(('localhost', 5000))
    except BlockingIOError:
        pass

    request = 'GET %s HTTP/1.0\r\n\r\n' % path

    callback = lambda: connected(s, request)
    f = Future()
    f.callbacks.append(callback)
    selector.register(s.fileno(), EVENT_WRITE, data=f)


def connected(s, request):
    selector.unregister(s.fileno())
    # s is writeable
    s.send(request.encode())

    chunks = []
    callback = lambda: readable(s, chunks)
    f = Future()
    f.callbacks.append(callback)
    selector.register(s.fileno(), EVENT_READ, data=f)


def readable(s, chunks):
    global n_tasks

    # s is readable
    selector.unregister(s.fileno())
    chunk = s.recv(1000)
    if chunk:
        chunks.append(chunk)
        callback = lambda: readable(s, chunks)
        f = Future()
        f.callbacks.append(callback)
        selector.register(s.fileno(), EVENT_READ, data=f)
    else:
        body = (b''.join(chunks)).decode()
        print(body.split('\n')[0])
        n_tasks -= 1


start = time.time()
get('/foo')
get('/foo')
get('/bar')
get('/bar')

while n_tasks:
    events = selector.select()
    for event, mask in events:
        fut = event.data
        fut.resolve()

print('took %.1f sec' % (time.time() - start))
