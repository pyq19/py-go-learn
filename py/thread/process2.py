from multiprocessing import Process
import os

class MyProcess(Process):
    def __init__(self):
        print 'init ->', os.getpid()
        super(MyProcess, self).__init__()
    
    def run(self):
        print 'run ->', os.getpid()


if __name__ == '__main__':
    print 'parent ->', os.getpid()
    p = MyProcess()
    p.start()
    p.join()

# parent -> 1752
# init -> 1752
# run -> 1753
