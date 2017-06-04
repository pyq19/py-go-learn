# coding:utf8
# http://www.jianshu.com/p/933a22ac0eb7


class SimpleItemContainer(object):
    def __init__(self, id, item_containers):
        self.id = id
        self.data = {}
        for item in item_containers:
            self.data[item.id] = item

# SimpleItemContainer通过python内置类型Dict来存放数据，

# 不过到目前为止想要访问对应的数据还是得直接调用里面的字典，

# 没法像原生的字典一样方便的通过暴露出来的api访问数据。

# 当然也可以从头开始把完整的Dictionary Interface完全实现个遍，

# 不过在每个自定义的类似的容器中都来一套肯定不行，

# 这时候利用python内置的UserDict.DictMixin就是一个不错的方式

from UserDict import DictMixin

class BetterSimpleItemContainer(object, DictMixin):
    def __getitem__(self, id):
        return self.data[id]

    def __setitem__(self, id, value):
        self.data[id] = value

    def __delitem__(self, id):
        del self.data[id]

    def keys(self):
        return self.data.keys()


# 把一些基础和单一的功能
# 比如希望通过interface/protocol 实现的功能放进Mixin 模块里
class CommonEqualityMixin(object):
    def __eq__(self, other):
        return (isinstance(other, self.__class__)
            and self.__dict__ == other.__dict__)

    def __ne__(self, other):
        return not self.__eq__(other)


class Foo(CommonEqualityMixin):
    def __init__(self, item):
        self.item = item
