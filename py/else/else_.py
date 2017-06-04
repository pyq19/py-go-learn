# coding:utf8
# http://www.jianshu.com/p/4d68e6c4d71b


# 配合for/while 循环语句使用
def print_prime(n): # 打印素数
    for i in xrange(2, n):
        # found = True
        for j in xrange(2, i):
            if i % j == 0:
                # found = False
                break
        else:
            print '{} its a prime number'.format(i)
        # if found:
        #     print '{} its a prime number'.format(i)

print_prime(7)
# 2 its a prime number
# 3 its a prime number
# 5 its a prime number


# 配合try except 错误控制使用
def my_to_int(str_param):
    try:
        print int(str_param)
    except ValueError:
        print 'cannot convert {} to a integer'.format(str_param)
    else:
        print 'convert {} to integer successfully.'.format(str_param)
my_to_int('asd')
# cannot convert asd to a integer
my_to_int('123')
# 123
# convert 123 to integer successfully.
