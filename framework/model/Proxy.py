'''
Created on 2013-7-27

@author: Administrator
'''
import MySQLdb
import framework.config.mysql as db;
import sys


class Proxy(object):
    
    table = 'python_proxy'
    
    def __init__(self):
        
        self.conn = MySQLdb.connect(host=db.conf['host'], 
                                    user= db.conf['user'],
                                    passwd=db.conf['pwd'],
                                    db=db.conf['db'])
        self.cursor = self.conn.cursor();
    
    def execute(self, sql):
        if not sql:
            return False
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except:
            self.conn.rollback();
            return False
        return True
    
    
    def get_rows(self, sql):
        if not sql:
            return False
        result = self.execute(sql)
        if result:
            return self.cursor.fetchall()
        
        return False
    
    def get_total(self,where = None):
        sql = "select count(*) as total from " + self.table 
        if where:
            sql += " where " + where
            
        return ''
            
        
        
    def get_online_proxy(self):
        sql ="select ip from " + self.table + " where online=1 limit 1"
        return ''
    
    def add_proxy(self, data):
        for item in data:
            ip = item
            sql = "insert ignore into " + self.table + " set ip='" + ip + "',ctime=now(), online=2"
            print sql
            self.execute(sql);
      
        