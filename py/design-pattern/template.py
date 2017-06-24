# coding:utf8
# http://dongweiming.github.io/python-template.html


# 模板方法模式


# 根据不同需求处理的内容
ingredients = 'spam eggs apple'
line = '-' * 10


# 被模板方法调用的基础函数
def iter_elements(getter, action):
    '''循环处理的骨架'''
    # getter 是要迭代的数据, action 是要执行的函数
    for element in getter():
        action(element)
        print(line)


def rev_elements(getter, action):
    '''反向的'''
    for element in getter()[::-1]:
        action(element)
        print(line)


# 数据经过函数处理就是最后传给模板的内容
def get_list():
    return ingredients.split()

def get_lists():
    return [list(x) for x in ingredients.split()]

# 对数据的操作
def print_item(item):
    print(item)

# 反向处理数据
def reverse_item(item):
    print(item[::-1])

# 模板函数
def make_template(skeleton, getter, action):
    # 它抽象的传入了骨架， 数据，和子类的操作函数
    def template():
        skeleton(getter, action)
    return template

# 列表解析, 数据就是前面的2 种骨架（定义如何迭代，2个分割数据的函数，正反向打印数据的组合）
templates = [make_template(s, g, a)
    for g in (get_list, get_lists)
    for a in (print_item, reverse_item)
    for s in (iter_elements, rev_elements)]

# 执行
for template in templates:
    template()
