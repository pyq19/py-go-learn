#coding:utf8

from functools import wraps

import profile

def debug(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print 'args ->', args
        print 'kwargs ->', kwargs
        print 'local() ->', locals()
        ld = locals()
        print ld.get('func')()
        return func(*args, **kwargs)
    return wrapper


class Trace(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print '<{name}>'.format(name=self.func.__name__)
        print 'args:{args}'.format(args=args)
        print 'kwargs:{kwargs}'.format(kwargs=kwargs)
        print 'Key-Values:{kw}'.format(kw=locals())
        print 'Output:{op}'.format(op=self.func(*args, **kwargs))
        print '=========='
        profile.run(self.func.__name__)

