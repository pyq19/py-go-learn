from multiprocessing import Pool

def test(*args, **kw):
    print args
    print kw
    return 123

if __name__ == '__main__':
    po = Pool()
    print po.apply(test, range(3), dict(a=1, b=2))
    po.close()
    po.join()

# (0, 1, 2)
# {'a': 1, 'b': 2}
# 123
