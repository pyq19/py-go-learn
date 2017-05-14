#coding:utf8

# Python 2
# http://www.binarytides.com/code-chat-application-server-client-sockets-python/

# TCP Chat server
# 1. Accept multiple incoming connections for client.
# 2. Read incoming messages from each client and 
#    broadcast them to all other connected clients.

import socket, select

# Function to broadcast chat message to all connected clients
def broadcast_data(sock, msg):
    # Do not send the message to master socket
    # and the client who has send us the message
    for socket in CONNECTION_LIST:
        if socket != server_socket and socket != sock:
            try:
                socket.send(msg)
            except:
                # broken socket connection may be,
                # chat client pressed ctrl+c for example
                socket.close()
                CONNECTION_LIST.remove(socket)

if __name__ == '__main__':
    
    # List to keep track of socket descriptors
    CONNECTION_LIST = []
    RECV_BUFFER = 4096  # Advisable to keep it as an exponent of 2
    PORT = 5000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # this has no effect..? wtf ??
    # !!! 
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('0.0.0.0', PORT))
    server_socket.listen(10)

    # Add server socket to the list of readable connections
    CONNECTION_LIST.append(server_socket)

    print 'Chat server started on port -->', str(PORT)

    while True:
        # Get the list sockets which are ready to be read through select
        # !!! select.select()
        read_sockets, write_sockets, error_sockets = select.select(
            CONNECTION_LIST, [], []
        )
        for sock in read_sockets:
            # New connection
            if sock == server_socket:
                # Handle the case in which there is a
                # new connection received through server_socket
                sockfd, addr = server_socket.accept()
                CONNECTION_LIST.append(sockfd)
                print 'Client (%s, %s) connected' % addr
                broadcast_data(sockfd, '[%s %s] entered room\n' % addr)

            # Some incoming message from a client
            else:
                # Data received from client, process it
                try:
                    data = sock.recv(RECV_BUFFER)
                    if data:
                        broadcast_data(sock, '\r' + '<' + str(sock.getpeername()) + '> ' + data)

                except:
                    broadcast_data(sock, 'Client (%s, %s) is offline' % addr)
                    print 'client %s offline' % addr
                    sock.close()
                    CONNECTION_LIST.remove(sock)
                    continue
    server_socket.close()
