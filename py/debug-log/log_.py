# coding:utf8
# https://my.oschina.net/jhao104/blog/668965


import logging


def get_logger(log_name, level=logging.INFO):
    # 创建一个logger
    logger = logging.getLogger(log_name)
    logger.setLevel(level)

    # 创建文件处理器
    file_handler = logging.FileHandler('%s.log' % log_name.upper())
    file_handler.setLevel(logging.INFO)
    # 创建输出处理器
    stream_handler = logging.StreamHandler()

    # 定义输出格式
    formatter = logging.Formatter('%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s:%(message)s')
    file_handler.setFormatter(formatter)
    stream_handler.setFormatter(formatter)

    # 给logger 添加处理器
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    return logger


if __name__ == '__main__':
    logger = get_logger('log')
    logger.warning('warn message')
    logger.info('info message')
    logger.debug('debug message')
