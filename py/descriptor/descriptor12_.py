# coding:utf8

import urlparse


class URLFieldProxy(unicode):
    @property
    def hostname(self):
        return urlparse.urlparse(self).hostname


class ProxyFieldDescriptor(object):
    def __init__(self, field_name, proxy_class):
        self.field_name = field_name
        self.proxy_class = proxy_class

    def __get__(self, instance=None, owner=None):
        value = instance.__dict__[self.field_name]
        if value is None:
            return value
        return self.proxy_class(value)

    def __set__(self, instance, value):
        instance.__dict__[self.field_name] = value


class SomeObject(object):
    wormhole = ProxyFieldDescriptor('url', URLFieldProxy)

    def __init__(self, url):
        self.url = url


if __name__ == '__main__':
    obj = SomeObject('http://example.com/asdf')
    print obj.url
    # print obj.url.hostname

    print obj.wormhole
    print obj.wormhole.hostname
