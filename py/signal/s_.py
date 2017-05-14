# Python 3.6

import signal, os

def handler(signum, frame):
    print('Signal handler called with a signal', signum)
    raise OSError("Couldn't open device!")

# Set the signal handler and 5-second alarm
signal.signal(signal.SIGALRM, handler)
signal.alarm(5)

# This open() may bang indefinitely
fd = os.open('./temp.txt', os.O_RDWR)

signal.alarm(0)     # Disable the alarm
