# coding:utf8
# https://www.blog.pythonlibrary.org/2016/06/09/python-how-to-create-an-exception-logging-decorator/


import functools
import logging


def create_logger():
    '''creates a logging object and returns it'''
    logger = logging.getLogger('example_logger')
    logger.setLevel(logging.INFO)

    # create the logging file handler
    fh = logging.FileHandler('exception_deco.log')

    fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    formatter = logging.Formatter(fmt)
    fh.setFormatter(formatter)

    # add handler to logger object
    logger.addHandler(fh)
    return logger


def exception(function):
    ''' a decorator that wraps the passed in function and logs
        exceptions should one occur '''
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        logger = create_logger()
        try:
            return function(*args, **kwargs)
        except:
            # log the exception
            err = 'there was an exception in'
            err += function.__name__
            logger.exception(err)

            # re-raise the exception
            raise
    return wrapper


@exception
def zero_divide():
    1 / 0


if __name__ == '__main__':
    zero_divide() 
