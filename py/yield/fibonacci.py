class Fibonacci(object):
    def __init__(self):
        self.numbers = []

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.numbers) < 2:
            self.numbers.append(1)
        else:
            self.numbers.append(sum(self.numbers))
            self.numbers.pop(0)
        return self.numbers[-1]

    def send(self, value):
        pass

    # for Python 2 compatibility
    next = __next__

f = Fibonacci()

i = iter(f)

print next(i), next(i), next(i), next(i), next(i)
# 1 1 2 3 5

i2 = iter(f)

print next(i2)
# 8
