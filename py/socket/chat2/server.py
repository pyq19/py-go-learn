#coding:utf8
# https://github.com/danielcardeenas/PythonChat/blob/master/Multi/servermul.py

import sys, socket, threading, string
import select

pin = 'ABC'

def xor(string, key):
    data = ''
    for char in string:
        for ch in key:
            char = chr(ord(char) ^ ord(ch))
        data += char
    return data

def broadcast(sock, msg, usr):
    for socket in CLIST:
        if socket != server_socket and socket != sock:
            print 'From: ', usr
            print 'MEssage received: ', msg
            print 'Broadcastring..\n'
            socket.send(msg)

if __name__ == '__main__':
    CLIST = []  # List fo sockets

    print '== TCP server =='
    port = str(raw_input('enter Ip to bind server -> '))
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((port, 5000))
    server_socket.listen(10)

    CLIST.append(server_socket) # Add socket

    while True:
        # Get list of ready to be read with select
        read_sockets, write_sockets, error_sockets = \
        select.select(CLIST, [], [])

        for sock in read_sockets:
            if sock == server_socket:
                sockfd, addr = server_socket.accept() # new connection received
                CLIST.append(sockfd)            # append new connection
                print 'client %s, %s connected' % addr
                # broadcast(sockfd, 'new client connected', addr)
            else:
                try:
                    data = sock.recv(4096, )
                except:
                    broadcast(sock, 'client %s %s is offline' % addr, addr)
                    print 'client %s %s is offline...' % addr
                    sock.close()
                    CLIST.remove(sock)
                    continue
                
                if data:        # client send data
                    if data == 'q' or data == 'Q': # if client quit
                        print 'client %s %s quit' % addr
                        sock.close()                # close socket
                        CLIST.remove(sock)          # remove from our list
                    else:
                        broadcast(sock, data, addr)

    server_socket.close()
