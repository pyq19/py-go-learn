from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
from queue import Queue


def echo_client(q):
    '''
    handle a client connection
    '''
    sock, client_addr = q.get()
    print('got connection from ->', client_addr)
    while True:
        msg = sock.recv(65536)
        if not msg:
            break
        sock.sendall(msg)
    print('client close connections ...')
    sock.close()

def echo_server(addr, nworkers):
    # launch the client workers
    q = Queue()
    for n in range(nworkers):
        t = Thread(target=echo_client, args=(q,))
        t.daemon = True
        t.start()

    # run the server
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(addr)
    sock.listen(5)
    while True:
        client_sock, client_addr = sock.accept()
        q.put((client_sock, client_addr))

echo_server(('', 15000), 128)
