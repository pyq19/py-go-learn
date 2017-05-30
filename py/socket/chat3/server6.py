import socket

def main():
    host = ''
    port = 9000

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))

    s.listen(2)

    c, addr = s.accept()

    while 1:
        data = c.recv(20)
        if not data:
            break
        print 'recv data ->', data
        back = str(data).upper()
        c.send(back)
        print 'send back ->', back
    c.close()

if __name__ == '__main__':
    main()
        
