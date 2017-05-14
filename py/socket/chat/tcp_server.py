# 3

import socket, select

def broadcast_data(message):
    for sock in CONNECTION_LIST:
        if sock != SERVER_SOCKET: # send message to everyone except the server
            try:
                sock.sendall(message)   # send all data at once
            except Exception as err:
                print(type(err).__name__)
                sock.close()
                try:
                    CONNECTION_LIST.remove(sock)
                except ValueError as err:
                    print('{}:{}'.format(type(err).__name__, err))

CONNECTION_LIST = []
RECV_BUFFER = 4096 # Advisable to keep it as an exponent of 2
PORT = 5000

SERVER_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER_SOCKET.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
SERVER_SOCKET.bind(('', PORT)) # empty addr string means INADDR_ANY

print('listening...')
SERVER_SOCKET.listen(10) # 10 connections

CONNECTION_LIST.append(SERVER_SOCKET)
print('server started...')

while True:
    # Get the list sockets which are ready to be read through select
    READ_SOCKETS, WRITE_SOCKETS, ERROR_SOCKETS = select.select(\
        CONNECTION_LIST, [], [])
    for SOCK in READ_SOCKETS: # new connection
        # handle the case in which there is a new connection
        # received through server_socket
        if SOCK == SERVER_SOCKET:
            SOCKFD, ADDR = SERVER_SOCKET.accept()
            CONNECTION_LIST.append(SOCKFD) # add socket descriptor(描述符号)
            # Adding \r to prevent message overlapping(重叠) when another
            # user types it's message
            print('\rClient {0}, {1} connected..'.format(ADDR[0], ADDR[1]))
            broadcast_data('client {0} {1} entered room\n'.format(ADDR[0], ADDR[1]).encode())
        else: # some incoming message from a client
            try:    # Data received from client, process it
                DATA = SOCK.recv(RECV_BUFFER)
                if DATA:
                    ADDR = SOCK.getpeername() # get remote address of the socket
                    message = '\r{}:{} : {}'.format(ADDR[0], ADDR[1], DATA.decode())
                    print(message, err='')
                    broadcast_data(message.encode())
            except Exception as msg:    # Errors happended, client disconnected.
                print(type(msg).__name__, msg)
                print("\rClient ({0}, {1}) disconnected.".format(ADDR[0], ADDR[1]))
                broadcast_data('\rClient ({0}, {1}) is offline\n'.format(ADDR[0], ADDR[1]).encode())
                SOCK.close()
                try:
                    CONNECTION_LIST.remove(SOCK)
                except ValueError as msg:
                    print('{}:{}'.format(type(msg).__name__, msg))
                continue

SERVER_SOCKET.close()
