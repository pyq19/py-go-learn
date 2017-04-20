class MyDog(object):
    def __len__(self):
        return 100

dog = MyDog()
print(len(dog)) # 100


# getattr() setattr() hasattr()
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x

obj = MyObject()
print(hasattr(obj, 'x')) # True

print(hasattr(obj, 'y')) # False

setattr(obj, 'y', 233)
print(hasattr(obj, 'y')) # True

print(getattr(obj, 'y')) # 233

print(obj.y) # 233

# getattr(obj, 'z') # AttributeError

# getattr可以传入一个default参数，如果属性不存在就返回默认值
print(getattr(obj, 'z', 404)) # 404

# 获得对象方法
print(hasattr(obj, 'power')) # True

print(getattr(obj, 'power')) 
# <bound method MyObject.power of <__main__.MyObject object at 0x10228ac88>>

fn = getattr(obj, 'power') # fn 指向obj.power
print(fn()) # 81
