'''
Created on 2013-7-27

@author: Administrator
'''
#-*-coding:utf-8-*-  
import threading,time,datetime  
import MySQLdb  

from DBUtils import PooledDB  
pool = PooledDB.PooledDB(MySQLdb,100,50,100,490,False,
host='localhost',user='root',passwd='321',db='test',
charset='utf8')   