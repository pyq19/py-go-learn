# coding:utf8
# http://dongweiming.github.io/python-memento.html


# python 设计模式 备忘录模式
# 事务提交例子

import copy

def Memento(obj, deep=False):
    # 对要做快照的对象做快照
    state = (copy.copy if deep else copy.deepcopy)(obj.__dict__)
    
    def Restore():
        obj.__dict__ = state
    return Restore


class Transaction:
    deep = False
    def __init__(self, *targets):
        self.targets = targets
        self.Commit()
    # 模拟事务提交，即初始化每个对象，往self.targets 赋值
    def Commit(self):
        self.states = [Memento(target, self.deep) for target in self.targets]
    # 回滚就是调用Memento 函数，执行其中的闭包，将__dict__ 恢复
    def Rollback(self):
        for state in self.states:
            state()


# 装饰器的方式给方法添加这个事务的功能
def transactional(method):
    # 此处self即要保存的对象，与类实例无关
    def wrappedMethod(self, *args, **kwargs):
        state = Memento(self)
        try:
            return method(self, *args, **kwargs)
        except:
            # 同上回滚一样，异常就恢复
            state()
            raise
    return wrappedMethod


class NumObj(object):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return '<%s: %r>' % (self.__class__.__name__, self.value)

    def Increment(self):
        self.value += 1

    @transactional
    def DoStuff(self):
        # 赋值成字符串，再自增长肯定会报错
        self.value = 'aaaaa'
        self.Increment()

if __name__ == '__main__':
    n = NumObj(-1)
    print n
    t = Transaction(n)
    try:
        for i in xrange(3):
            n.Increment()
            print n
        # 这里事务提交会保存状态从第一次-1 到2 
        t.Commit()
        print '-- commited'
        for i in xrange(3):
            n.Increment()
            print n
        n.value += 'x' # ERROR !!!
        print n
    except:
        # 回滚只会到上次commit 成功的2 而不是-1
        t.Rollback()
        print '-- rolled back'
    print n
    print '-- now doing stuff ..'
    try:
        n.DoStuff()
    except:
        print '-> doing stuff failed!!'
        import traceback
        traceback.print_exc(0)
        pass
    # 第二次异常回滚n 还是2，整个过程都是修改NumObj 实例对象
    print n

# <NumObj: -1>
# <NumObj: 0>
# <NumObj: 1>
# <NumObj: 2>
# -- commited
# <NumObj: 3>
# <NumObj: 4>
# <NumObj: 5>
# -- rolled back
# <NumObj: 2>
# -- now doing stuff ..
# -> doing stuff failed!!
# Traceback (most recent call last):
# TypeError: cannot concatenate 'str' and 'int' objects
# <NumObj: 2>

# 若要保存的状态很大会浪费大量内存
