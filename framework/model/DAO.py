'''
Created on 2013-7-20

@author: Administrator
'''
import MySQLdb
import framework.config.mysql as db;
import sys

class DAO(object):
    table = 'user'
    
    def __init__(self):
        self.conn = MySQLdb.connect(host=db.conf['host'], 
                                    user= db.conf['user'],
                                    passwd=db.conf['pwd'],
                                    db=db.conf['db'])
        self.cursor = self.conn.cursor();
        print self.cursor
    def insert(self, data):
        if not data:
            return False
        sql = "insert into " + self.table + " set "
        for k, v in enumerate(data):
            
            sql += v + "='" + str(data[v]) + "',"
            
        sql = sql.strip(',')
        print sql
        return self.execute(sql)
     
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
    
    def update(self, source, filter_array = None):
        if not source:
            return False
        
        sql = "update " + self.table + " set "
        for k, v in enumerate(source):
            
            sql += v + "='" + str(source[v]) + "',"
            
        sql = sql.strip(',')
        
        if filter_array:
            where = ''
            for k, v in enumerate(filter_array):
                where += v + "='" + str(filter_array[v]) + "',"
            where = where.strip(',')
            if where:
                sql += " where " + where
        
        
        print sql
        return self.execute(sql)
    
    
    def delete(self, filter_array = None):
        if not filter_array:
            return False
        
        sql = "delete from " + self.table
       
        if filter_array:
            where = ''
            for k, v in enumerate(filter_array):
                where += v + "='" + str(filter_array[v]) + "',"
            where = where.strip(',')
            if where:
                sql += " where " + where
        
        print sql
        return self.execute(sql)
    
    
    def destroy(self):        
        self.conn = None
        self.cursor = None
         
            
        
    