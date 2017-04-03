from abc import ABCMeta, abstractmethod


class IStream(metaclass=ABCMeta):
    @abstractmethod
    def read(self, maxbytes=-1):
        pass

    @abstractmethod
    def write(self, data):
        pass


class SocketStream(IStream):
    def read(self, maxbytes=-1):
        print('read')

    def write(self, data):
        print('write')


def serialize(obj, stream):
    if not isinstance(stream, IStream):
        raise TypeError('Expected an IStream...')
    pass


import io

# Register the build-in I/O classes as supporting our interface
IStream.register(io.IOBase)

# Open a normal file and type check
f = open('foo.txt')
print(isinstance(f, IStream))  # Return True
