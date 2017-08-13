# coding:utf8
# https://www.youtube.com/watch?v=7sCu4gEjH5I&list=PLTOBJKrkhpoMdsT9RUERSDdEVrViykAEQ&index=1



from selectors import DefaultSelector, EVENT_WRITE, EVENT_READ
import socket
import time

selector = DefaultSelector()
n_tasks = 0


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
    selector.register(s.fileno(), EVENT_WRITE, data=callback)
    selector.select()


def connected(s, request):
    selector.unregister(s.fileno())
    # s is writeable
    s.send(request.encode())

    chunks = []
    callback = lambda: readable(s, chunks)
    selector.register(s.fileno(), EVENT_READ, data=callback)


def readable(s, chunks):
    global n_tasks

    # s is readable
    selector.unregister(s.fileno())
    chunk = s.recv(1000)
    if chunk:
        chunks.append(chunk)
        callback = lambda: readable(s, chunks)
        selector.register(s.fileno(), EVENT_READ, data=callback)
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
        cb = event.data
        cb()

print('took %.1f sec' % (time.time() - start))
