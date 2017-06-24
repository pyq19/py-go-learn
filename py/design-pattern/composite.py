# coding:utf8
# http://dongweiming.github.io/python-composite.html


# 组合模式
# 把composite 模式看成一个复杂的属性结构，
# 其实基本有三种角色：树干（定义操作树叶leaf的操作）
# 树枝（树干上有很多树枝） 树叶（树干想要具体操作的对象）


class Trunk(object):
    '''树干'''
    def __str__(self):
        pass

    def subtree(self):
        pass


class Composite(Trunk):
    
    def __init__(self, left=None, right=None, length=None):
        self.left = left
        self.right = right
        self.length = length

    def __str__(self):
        # 这个结果是在调用subtree() 的时候返回
        if self.length:
            return '(' + self.left.__str__() + ', ' + self.right.__str__() + ')' + ': ' + str(self.length)
        else:
            return '(' + self.left.__str__() + ', ' + self.right.__str__() + ')'

        # 通过这个函数返回下一级的对象，即它既是对象还可以是对象的容器
        def subtree(self):
            return Composite(self.left, self.right)


class Leaf(Trunk):
    '''叶子类，它无法继续延伸'''
    def __init__(self, name, length=None):
        self.name = name
        self.length = length
        self.left = None
        self.right = None

    def __str__(self):
        return self.name + ': ' + str(self.length)

    def subtree(self):
        return Leaf(self.name, self.length)


if __name__ == '__main__':
    # 只有叶子那么就直接返回__str__ 的拼装结果
    t1 = Leaf('A', 0.71399)
    print t1
    # 有个2个叶子的组合，返回的是2个叶子的对象组合
    t2 = Composite(Leaf('B', -0.00804),
        Leaf('C', 0.07470))
    print t2
    # 这个是嵌套的叶子的组合，树干上面有树枝，树枝上面有叶子
    t3 = Composite(Leaf('A', 0.71399),
        Composite(Leaf('B', -0.00804),
            Leaf('C', 0.07470), 0.1533), 0.0666)

    print t3
    # 直接通过左右节点找到对应的叶子对象
    t4 = t3.right.right.subtree()
    print t4
    # t3 的左树其实就是叶子对象
    t5 = t3.left.subtree()
    print t5
