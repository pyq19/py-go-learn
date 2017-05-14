#coding:utf8

import socket

HOST = '127.0.0.1'
PORT = 5000
EOL1 = b'\r\n'
EOL2 = b'\r\n\r\n'

sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((HOST, PORT))
sock.listen(1)

while True:
    try:
        data = b''
        connection, address = sock.accept()
        while True:
            data += connection.recv(4096)
            if EOL1 in data or EOL2 in data:
                break
        connection.sendall(data)
        connection.close()
    finally:
        connection.close()
