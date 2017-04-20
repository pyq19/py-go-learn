#coding:utf8

# Python 默认采用 引用计数 来管理对象的内存回收，
# 当引用计数为0时，将立即回收该对象内存
# 要么将对应的block块标记为空闲，要么返还给操作系统

class User(object):
    def __del__(self):
        print 'will be dead !!'

# >>> from del_ import User
# >>> a = User()
# >>> b = a
# >>> import sys
# >>> sys.getrefcount(a)
# 3
# >>> del a # 删除引用，计数减少 
# >>> sys.getrefcount(b)
# 2
# >>> del b # 删除最后一个引用，计数器为0，对象被回收
# will be dead !!


# 用弱引用回调监控对象回收

# >>> import sys, weakref
# >>> class User(object): pass
# ...
# >>> def callback(r):                  # 回调函数会在原对象被回收时调用
# ...     print 'weakref object ->', r
# ...     print 'target object dead !'
# ...
# >>> a = User()
# >>> r = weakref.ref(a, callback)      # 创建弱引用对象
# >>> sys.getrefcount(a)                # 弱引用没有导致目标对象引用计数增加
# 2                                     # 计数2是因为getrefcount形参造成的
# >>> r() is a                          # 透过弱引用可以访问原对象
# True
# >>> del a                             # 原对象回收，callback被调用
# weakref object -> <weakref at 0x1004163c0; dead>
# target object dead !
# >>> hex(id(r))                        # 对比可以看到callback参数是弱引用对象
# '0x1004163c0'                         # 因为原对象已经死亡
# >>> r() is None                       # 此时弱引用只能返回None，判断原对象死亡
# True
