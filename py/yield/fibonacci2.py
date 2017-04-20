def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b # !
        a, b = b, a + b
        n = n + 1
    return 'done...'
   
def fib2(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b) # !
        a, b = b, a + b
        n = n + 1
    return 'done .....'

if __name__ == '__main__':
    for n in fib(6):
        print(n)
    print('*' * 10)
    fib2(6)
# 1
# 1
# 2
# 3
# 5
# 8
# **********
# 1
# 1
# 2
# 3
# 5
# 8
