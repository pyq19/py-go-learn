# coding:utf8
# http://mingxinglai.com/cn/2015/08/python-decorator/#top


class Store(object):
    
    def get_food(self, username, food):
        if username != 'admin':
            raise Exception('this user is not allowed to get food')
        return self.storage.get(food)

    def put_food(self, username, food):
        if username != 'admin':
            raise Exception('this user is not allowed to put food')
        self.storage.put(food)


##############


def check_is_admin(username):
    if username != 'admin':
        raise Exception('this user is not allowed to get food')


class Store(object):
    def get_food(self, username, food):
        check_is_admin(username)
        return self.storage.get(food)

    def put_food(self, username, food):
        check_is_admin(username)
        return self.storage.put(food)


##################


def check_is_admin(func):
    def wrapper(*args, **kwargs):
        if kwargs.get('username') != 'admin':
            raise Exception('this user is not allowed to get food')
        return func(*args, **kwargs)
    return wrapper


class Storage(object):
    @check_is_admin
    def get_food(self, username, food):
        return self.storage.get(food)

    @check_is_admin
    def put_food(self, username, food):
        return self.storage.put(food)
