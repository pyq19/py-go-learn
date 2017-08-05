# coding:utf8
# https://www.youtube.com/watch?v=7sCu4gEjH5I&list=WL&index=1

from selectors import DefaultSelector, EVENT_WRITE, EVENT_READ
import time
import socket

selector = DefaultSelector()

def get(path):
    s = socket.socket()
    s.setblocking(False)

    try:
        s.connect(('localhost', 5000))
    except BlockingIOError:
        pass

    request = f'GET {path} HTTP/1.0\r\n\r\n'

    selector.register(s.fileno(), EVENT_WRITE)
    selector.select()
    selector.unregister(s.fileno())

    # s is writable
    s.send(request.encode())

    chunks = []
    while True:
        selector.register(s.fileno(), EVENT_READ)
        selector.select()
        selector.unregister(s.fileno())

        chunk = s.recv(1000)
        if chunk:
            chunks.append(chunk)
        else:
            body = (b''.join(chunks)).decode()
            print(body.split('\n')[0])
            return


start = time.time()
get('/foo')
get('/bar')
end = time.time()
print('took %.1f sec' % (end - start))
