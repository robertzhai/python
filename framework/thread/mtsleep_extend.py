'''
Created on 2013-8-10

@author: Administrator
'''
import threading
from time import sleep, ctime

loops = (4, 2)

class MyThread(threading.Thread):
    
    def __init__(self, func, args, name = ''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args
    
    def run(self):
        self.func(*self.args)
    

def loop(nloop, nsec):
    print 'start loop', nloop, ' at:',ctime()
    sleep(nsec)
    print 'loop', nloop, ' done at:',ctime()
    
def main():
    print 'starting st:',ctime()
    threads = []
    nloops = range(len(loops))
    
    for i in nloops:
        t = MyThread(loop,(i,loops[i]), loop.__name__)
        threads.append(t)
        
    for i in nloops:
        threads[i].start()
        
    print ' all done at:',ctime()

if __name__ == '__main__':
    main()
















