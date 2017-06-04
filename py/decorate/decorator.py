# coding:utf8
# http://python.jobbole.com/86717/

def say_hello():
    print 'hello'

def say_goodbye():
    print 'byebye'

if __name__ == '__main__':
    say_hello()
    say_goodbye()

#########################

def debug():
    import inspect
    caller_name = inspect.stack()[1][3]
    print 'debug -> enter {}()'.format(caller_name)

def say_hello():
    debug()
    print 'hello'

def say_goodbye():
    debug()
    print 'byebye'

if __name__ == '__main__':
    say_hello()
    say_goodbye()

#############################

def debug(func):
    def wrapper():
        print 'debug -> enter {}()'.format(func.__name__)
        return func()
    return wrapper

def say_hello():
    print 'hello'

say_hello = debug(say_hello)

# 等同于
@debug
def say_hello():
    print 'hello'

#################################


def debug(func):
    def wrapper(*args, **kwargs):
        print 'debug -> enter {}()'.format(func.__name__)
        return func(*args, **kwargs)
    return wrapper
    
#################################

def logging(level):
    def wrapper(func):
        def inner_wrapper(*args, **kwargs):
            print '[{level}] -> enter function {func}()'.format(level=level, func=func.__name__)
            return func(*args, **kwargs)
        return inner_wrapper
    return wrapper

@logging(level='INFO')
def say(something):
    print 'say {}'.format(something)

# 等同于
# say = logging(level='INFO')(say)

@logging(level='DEBUG')
def do(something):
    print 'do {}..'.format(something)

if __name__ == '__main__':
    say('hello')
    do('my work')

#################################

#TODO 基于类实现的装饰器
