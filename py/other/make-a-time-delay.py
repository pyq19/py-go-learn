import time
print 'delay 5s'
time.sleep(5) # delays for 5 seconds


while True:
    print 'in the loop'
    loop_times = 1
    while True:
        print 'loop %s times' % loop_times
        print 'This prints once 2 seconds'
        time.sleep(2)
        loop_times += 1

from time import sleep
sleep(0.5)
