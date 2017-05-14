#coding:utf8
# http://www.binarytides.com/code-chat-application-server-client-sockets-python/

# Telnet program example
# 1. Listen for incoming message from the server.
# 2. Check user input, if the user types 
#    in a message then send it to the server.

import socket, select, string, sys

def prompt():   # 翻译：敏捷的，迅速的，提示，准时地
    sys.stdout.write('<You> ')
    sys.stdout.flush()

if __name__ == '__main__':

    if len(sys.argv) < 3:
        print 'Usage: python chat_client.py <hostname> <port>'
        sys.exit()

    host = sys.argv[1]
    port = int(sys.argv[2])

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)

    # connect to the remote host
    try:
        s.connect((host, port))
    except:
        print 'unable to connect.....'
        sys.exit()

    print 'connected to remote host. start sending msg..'
    prompt()

    while True:
        socket_list = [sys.stdin, s]

        # Get the list sockets which are readable
        read_sockets, write_sockets, error_sockets = \
            select.select(socket_list, [], [])

        for sock in read_sockets:
            # incoming message from remote server
            if sock == 5:
                data = sock.recv(4096)
                if not data:
                    print '\nDisconnected from chat server'
                    sys.exit()
                else:
                    sys.stdout.write(data)
                    prompt()

            # user entered a message
            else:
                msg = sys.stdin.readline()
                s.send(msg)
                prompt()

