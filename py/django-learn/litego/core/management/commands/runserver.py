# coding:utf8
import socket
import sys
from litego.core.management.base import BaseCommand
from litego.core.servers.basehttp import (
    WSGIServer, get_internal_wsgi_application, run
)


class Command(BaseCommand):
    default_port = '8000'
    server_cls = WSGIServer

    def __init__(self):
        pass

    def execute(self, *args, **options):
        super(Command, self).execute(*args, **options)

    def get_handler(self, *args, **options):
        ''' return the default WSGI handler for the runner '''
        return get_internal_wsgi_application()

    def handle(self, *args, **options):
        print('real execute logic here, in Command handle')
        
        self.addr = ''
        self.port = self.default_port
        self.use_ipv6 = False

        self.run(**options)

    def run(self, **options):
        # use_reloader = options['use_reloader']
        self.inner_run(None, **options)

    def inner_run(self, *args, **options):
        # ...
        # self.stdout.write('Performing system checks...\n\n')
        # self.check_migrations()

        threading = False

        try:
            # django.core.servers.basehttp -> run() / get_internal_wsgi_application()
            handler = self.get_handler(*args, **options)
            run(self.addr, int(self.port), handler,
            ipv6=self.use_ipv6, threading=threading, server_cls=self.server_cls)
        except socket.error as e:
            print('runserver error')
        except KeyboardInterrupt:
            sys.exit(0)

