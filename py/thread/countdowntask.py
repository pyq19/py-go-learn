from threading import Thread
import time

class CountDownTask:
    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self, n):
        while self._running and n > 0:
            print('T-minus', n)
            n -= 1
            time.sleep(5)

c = CountDownTask()
t = Thread(target=c.run, args=(10,))
t.start()
print('.....')
c.terminate()
t.join()
