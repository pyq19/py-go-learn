from threading import Thread
from socket import socket, AF_INET, SOCK_STREAM


def echo_client(sock, client_addr):
    '''
    handle a client connection
    '''
    print('get connection from ->', client_addr)
    while True:
        msg = sock.recv(65536)
        if not msg:
            break
        sock.sendall(msg)
    print('client closed connection..')
    sock.close()

def echo_server(addr, nworkers):
    # run the server
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(addr)
    sock.listen(5)
    while True:
        client_sock, client_addr = sock.accept()
        t = Thread(target=echo_client, args=(client_sock, client_addr))
        t.daemon = True
        t.start()

echo_server(('', 15000))
