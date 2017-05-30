import socket

def main():
    host = '172.17.0.2'
    port = 9000

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    msg = raw_input('-> ')
    while msg != 'q':
        s.send(msg)
        data = s.recv(20)
        print 'recv from server ->', data
        msg = raw_input('-> ')
    s.close()

if __name__ == '__main__':
    main()


