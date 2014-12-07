'''
Created on 2013-7-20

@author: Administrator
'''
import MySQLdb
import framework.config.mysql as db;

print  db.conf


conn = MySQLdb.connect(host=db.conf['host'], 
                                    user= db.conf['user'],
                                    passwd=db.conf['pwd'],
                                    db=db.conf['db'])
cursor = conn.cursor();
try:
    print cursor.execute("insert into user set age='1216',name='robert'")
    conn.commit()
except:
    conn.rollback();
    
    
print cursor.execute("select * from user")

res = cursor.fetchall()
print res
cursor.close()
conn.close()