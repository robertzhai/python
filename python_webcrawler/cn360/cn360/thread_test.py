'''
Created on 2013-12-21

@author: Administrator
'''

import threading,time
import sys


class MyThread(threading.Thread):
    
    name = ''
    url = ''
    
    def __init__(self,threadname,url):
        threading.Thread.__init__(self)
        self.name = threadname
        self.url = url

    def run(self):
        time.sleep(1)
        print self.name


thread_num = 10
threads = []
for num in xrange(thread_num):
    threads.append(MyThread("threadd : %d " % num , num))
    
for num in xrange(thread_num):
    threads[num].start()
    threads[num].join()
    
print "ended"
    