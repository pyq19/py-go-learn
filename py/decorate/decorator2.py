# coding:utf8
# https://zhuanlan.zhihu.com/p/24449936


def wrapper(func):
    def inner(*args, **kwargs):
        print(func.__name__, *args, **kwargs)
        return func(*args, **kwargs)
    return inner

@wrapper
def print_func(words):
    return words

print_func('hihihi')
# print_func hihihi


# 需要缓存的地方
def get_article_detail(uid):
    article = ORM.get_article(uid)

    if article:
        cache.incr('key')
    return article


# 使用装饰器
def increase_page_view(func):
    def wrapper(*args, **kwargs):
        obj = func(*args, **kwargs)
        if obj:
            cache.incr(obj.id)
        return obj
    return wrapper

@increase_page_view
def get_article_detail(uid):
    return ORM.get_article(uid)
