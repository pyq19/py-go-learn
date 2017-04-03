from socket import socket, AF_INET, SOCK_STREAM


class LazyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = SOCK_STREAM
        self.connections = []

    def __enter__(self):
        sock = socket(self.family, self.type)
        sock.connect(self.address)
        self.connections.append(sock)
        return sock

    def __exit__(self, exc_ty, exc_val, tb):
        self.connections.pop().close()


from functools import partial

conn = LazyConnection(('localhost', 8000))

with conn as s1:
   s1.send(b'GET / HTTP/1.0\r\n')
   s1.send(b'Host: localhsot\r\n')
   s1.send(b'\r\n')
   resp = b''.join(iter(partial(s1.recv, 8192), b''))
   print resp

   with conn as s2:
       s2.send(b'GET / HTTP/1.0\r\n')
       s2.send(b'Host: localhsot\r\n')
       s2.send(b'\r\n')
       resp = b''.join(iter(partial(s2.recv, 8192), b''))
       print resp




