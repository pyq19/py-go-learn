# coding:utf8
# https://github.com/Vamei/Python-Tutorial-Vamei/blob/master/content/%E6%B7%B1%E5%85%A505%20%E8%A3%85%E9%A5%B0%E5%99%A8.md


# 计算平方和
def square_sum(a, b):
    return a**2 + b**2

# 计算平方差
def square_diff(a, b):
    return a**2 - b**2

print square_sum(3, 5)
print square_diff(3, 5)


############

# 为函数增加打印输出
def square_sum(a, b):
    print 'input ->', a, b
    return a**2 + b**2

def square_diff(a, b):
    print 'input ->', a, b
    return a**2 - b**2

print square_sum(3, 5)
print square_diff(3, 5)


###########

# 使用装饰器实现上述修改

def decorator(func):
    def wrapper(*args, **kwargs):
        print 'input ->', args
        return func(*args, **kwargs)
    return wrapper

@decorator
def square_sum(a, b):
    return a**2 + b**2

@decorator
def square_diff(a, b):
    return a**2 - b**2

print square_sum(3, 5)
print square_diff(3, 5)

