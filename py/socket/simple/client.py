#coding:utf8

import socket

host = '127.0.0.1'
port = 5000
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    s.sendall(b'Hello, world!')
    data = s.recv(4096)

print('received ->', data)
