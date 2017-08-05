# coding:utf8
# https://www.youtube.com/watch?v=7sCu4gEjH5I&list=WL&index=1


import socket


def get(path):
    s = socket.socket()
    s.connect(('localhost', 5000))

    request = 'GET %s HTTP/1.0\r\n\r\n' % path

    s.send(request.encode())

    chunks = []
    while True:
        chunk = s.recv(1000)
        if chunk:
            chunks.append(chunk)
        else:
            body = (b''.join(chunks)).decode()
            print(body.split('\n')[0])
            return

get('/foo')
