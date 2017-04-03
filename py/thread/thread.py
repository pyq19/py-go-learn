import time


# def countdown(n):
#     while n > 0:
#         print('T-mins', n)
#         n -= 1
#         time.sleep(.1)
# 
# 
# from threading import Thread
# t = Thread(target=countdown, args=(10,))
# t.start()


def countup(n):
    x = 0
    while x <= n:
        print('count up', x)
        x += 1
        time.sleep(.2)


from threading import Thread
t = Thread(target=countup, args=(5,))
t.start()
