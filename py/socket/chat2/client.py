#coding:utf8
# https://github.com/danielcardeenas/PythonChat/blob/master/Multi/clientmul.py

import socket, thread, sys

pin = 'ABC'

# !!!
def xor(string, key):
    data = ''
    for char in string:
        for ch in key:
            char = chr(ord(char) ^ ord(ch))
        data += char
    return data

def recv_data(): # Receive data from other clients connected to server
    while True:
        try:
            recv_data = client_socket.recv(4096)
        except:
            # Process terminates
            print 'server closed connection.....'
            thread.interrupt_main() # Interrupt main when socket closes
            break
        if not recv_data:    # If recv has no data, close connection (err)
            print 'server closed connectioin..'
            thread.interrupt_main()
            break
        else:
            print '\nReceived data: ', recv_data
            recv_data = xor(recv_data, pin)
            print 'Dectrypted data: ', recv_data

def send_data():
    while True:
        send_data = str(raw_input('> `q` to quit..\n'))
        if send_data == 'q' or send_data == 'Q':
            client_socket.send(send_data)
            thread.interrupt_main()
            break
        else:
            send_data = xor(send_data, pin)
            client_socket.send(send_data)

if __name__ == '__main__':
    print '== TCP client =='
    ip = str(raw_input('enter server IP to connect -> '))
    print 'connecting to ', ip, ':5000'
    user = str(raw_input('enter username -> '))
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((ip, 5000))

    thread.start_new_thread(recv_data, ())
    thread.start_new_thread(send_data, ())

    try:
        while True:
            continue
    except:
        print 'client quit..'
        client_socket.close()

