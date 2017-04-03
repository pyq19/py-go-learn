from wsgiref.simple_server import make_server

from app import application

if __name__ == '__main__':
    httpd = make_server('', 8000, application)
    httpd.serve_forever()
