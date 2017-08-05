class PrintNumber(object):
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
    # def next(self):
        if(self.num >= self.max):
            raise StopIteration
        self.num += 1
        return self.num

pn = PrintNumber(3)

pr_iter = iter(pn)

print(next(pr_iter))
print(next(pr_iter))
print(next(pr_iter))
print(next(pr_iter))
# 1
# 2
# 3
# StopIteration
