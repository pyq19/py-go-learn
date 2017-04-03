# 3

class A:
    def __init__(self):
        self.x = 0

class B(A):
    def __init__(self):
        super().__init__()
        self.y = 1

b = B()
print(b.x)
print(b.y)

# 0
# 1
