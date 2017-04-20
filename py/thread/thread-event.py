from threading import Thread, Event
import time


# code to execute in an independent thread
def countdown(n, started_evt):
    print('countdown starting...')
    started_evt.set()
    while n > 0:
        print('T-minus ->', n)
        n -= 1
        time.sleep(1)

# create the event object that will be used to signal startup
started_evt = Event()

# launch the thread and pass the startup event
print('launching countdown')
t = Thread(target=countdown, args=(10, started_evt))
t.start()

# wait for the thread to start
started_evt.wait()
print('countdown is running..')

# launching countdown
# countdown starting...
# T-minus -> 10
# countdown is running..
# T-minus -> 9
# T-minus -> 8
# T-minus -> 7
# T-minus -> 6
# T-minus -> 5
# T-minus -> 4
# T-minus -> 3
# T-minus -> 2
# T-minus -> 1
