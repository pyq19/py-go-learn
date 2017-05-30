# http://stackoverflow.com/questions/36901/what-does-double-star-and-star-do-for-parameters

# the *args will give you all function parameters `as a tuple`
def foo(*args):
    for a in args:
        print a

def bar(**kwargs):
    for a in kwargs:
        print a, kwargs[a]

if __name__ == '__main__':
    foo(1)
    print '=' * 10
    foo(1, 2, 3, 4, 5)
    print '=' * 10
    bar(A='AAA', cc='CCC')
    print '=' * 10
    d = {'name':'mcc', 'age':25}
    bar(**d)
# 1
# ==========
# 1
# 2
# 3
# 4
# 5
# ==========
# A AAA
# cc CCC
# ==========
# age 25
# name mcc
