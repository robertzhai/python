'''
Created on 2013-7-27

@author: Administrator
'''
import Queue

q = Queue.Queue()
q.put(2)
q.put(3)
q.put(13)
q.put(23)
print q
print q.get()
print q.get()
print q.get()
print q.get()