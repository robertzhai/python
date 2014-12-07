'''
Created on 2013-7-27

@author: Administrator
'''
import urllib,urllib2
from thread_pool import Worker
from thread_pool import WorkerManager
import sys
import framework.tool.FileHandler as FileHandler

def test_job(id, sleep = 0.001 ):   
   try:   
       html = urllib.urlopen('http://www.cnproxy.com/proxy%d.html' % (id)).read()   
       fh = FileHandler.FileHandler("proxy_{%d}.html" % id , "w")
       fh.file_put_contents(html)
       fh.close()
   except:   
       print '[%4d]' % id, sys.exc_info()[:2]   
   return id   
def test():   
   import socket   
   socket.setdefaulttimeout(10)   
   print 'start testing'   
   wm = WorkerManager(3)   
   for i in range(1,11):   
       wm.add_job( test_job, i, i*0.001 )   
   wm.wait_for_complete()   
   print 'end testing'
   
if  __name__ == '__main__' :
    test()