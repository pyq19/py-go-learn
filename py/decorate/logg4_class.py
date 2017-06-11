# coding:utf8
# http://docs.pythontab.com/interpy/decorators/deco_class/


from functools import wraps


class logit(object):
    def __init__(self, logfile='out.log'):
        self.logfile = logfile

    def __call__(self, func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_str = func.__name__ + ' was called'
            print log_str
            with open(self.logfile, 'a') as fi:
                fi.write(log_str + '\n')
            self.notify()
            return func(*args, **kwargs)
        return wrapped_function

    def notify(self):
        pass
        

class email_logit(logit):
    def __init__(self, email='xxx@xxx.com', *args, **kwargs):
        self.email = email
        super(logit, self).__init__(*args, **kwargs)

    def notify(self):
        # 发送一封邮件
        pass


@logit()
def myfunc1():
    pass
