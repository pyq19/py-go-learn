# coding:utf8
# https://www.blog.pythonlibrary.org/2016/06/09/python-how-to-create-an-exception-logging-decorator/


import logging


def create_logger():
    ''' creates a logging object and returns it '''
    logger = logging.getLogger('example_logger')
    logger.setLevel(logging.INFO)

    # create the logging file handler
    fh = logging.FileHandler(r'exception_logger.log')

    fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    formatter = logging.Formatter(fmt)
    fh.setFormatter(formatter)

    # add handler to logger object
    logger.addHandler(fh)
    return logger


logger = create_logger()


import functools


def exception(logger):
    ''' a decorator that wraps the passed in function and logs exceptions
        should one occur '''

    def decorator(func):
        
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except:
                # log the exception
                err = 'there was an exception in '
                err += func.__name__
                logger.exception(err)
            # re-raise the exception
            raise
        return wrapper
    return decorator


@exception(logger)
def zero_divide():
    1 / 0


if __name__ == '__main__':
    zero_divide()
