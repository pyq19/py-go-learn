# coding:utf8
# http://dongweiming.github.io/python-command.html


# 命令调度模式


# Command Dispatch

# # 场景 1
# if command == 'get':
#     get()
# elif command == 'put':
#     put()
# else:   
#     error()
# 
# # 场景 2 
# dispatch_table = {
#     'get': get,
#     'put': put,
# }
# 
# if dispatch_table.has_key(command):
#     func = dispatch_table[command]
#     func()
# else:
#     error()

# 场景 3
def greet(who):
    print 'hello %s' % who
    
greet_command = lambda: greet('world')
greet_command()
# hello world


# 场景 4 python 自带的cmd 库
class Dispatcher:
    
    def do_get(self):
        pass

    def do_put(self):
        pass

    def error(self):
        pass

    def dispatch(self, command):
        mname = 'do_' + command
        if hasattr(self, mname):
            method = getattr(self, mname)
            method()
        else:
            self.error()

# 例子
# 封装pymongo 的类，通过工厂方法模式执行insert/update/find 操作

from pymongo import MongoClient

class MongoPack(object):
    
    def __init__(self, db):
        self.db = db

    # 通过指定kind 标识操作的种类insert/find/update
    def operation(self, coll, kind, **kwargs):
        return getattr(self, kind)(coll, **kwargs)

    # 当指定kind 为'find' 执行这个方法
    def find(self, coll, **kwargs):
        print 'kwargs ->', kwargs
        return self.db[coll].find(kwargs)


if __name__ == '__main__':
    
    db = MongoClient()['test']
    d = MongoPack(db)
    query = {'$and': [{'item': 'postcard'}]}
    for i in d.operation('inventory', 'find', **query):
        print i

# kwargs -> {'$and': [{'item': 'postcard'}]}
# {u'item': u'postcard', u'_id': ObjectId('594cc769d9a192b5d12190a5'), u'instock': [{u'warehouse': u'B', u'qty': 15.0}, {u'warehouse': u'C', u'qty': 35.0}]}
