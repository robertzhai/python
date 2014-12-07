#-*- coding: utf-8 -*-

'''
Created on 2013-12-21

http://www.cn360cn.com/news.aspx?pageno=2
@author: Administrator
'''
import Pager
import Queue
import sys
import time
import threading

task_queue = Queue.Queue(10)

class ProducerThread(threading.Thread):
    
    
    def __init__(self,threadname):
        threading.Thread.__init__(self)
        self.name = threadname

    def run(self):
        for page in xrange(1,500):
            url = 'http://www.cn360cn.com/news.aspx?pageno=%d' % page
            task_queue.put(url)
            print "put %s " % url
            
        
class ConsumerThread(threading.Thread):
    
    name = ''
    url = ''
    
    def __init__(self,threadname):
        threading.Thread.__init__(self)
        self.name = threadname

    def run(self):
        
        while 1:
            print self.name
            page = Pager.Pager()
            url = task_queue.get()
            print "get %s " % url
            try:
                page.get_html(url)
            except Exception as e:
                print "exception occurred : " , e
            finally:
                task_queue.task_done()
            #控制速度
            time.sleep(0.5)


print "start crawing ...."

producer = ProducerThread("crawler producer ....")
producer.setDaemon(True)
producer.start()

thread_num = 60
threads = []
for num in xrange(thread_num):
    print "crawler consumer : %d " % num
    threads.append(ConsumerThread("crawler consumer : %d " % num))

for num in xrange(thread_num):
    threads[num].setDaemon(True)
    threads[num].start()

#只到所有任务完成后，才退出主程序
task_queue.join()

print "finished ...."
