'''
Created on 2013-7-19

@author: Administrator
'''
import framework.model.DAO as DAO;

dal = DAO.DAO();

sql = "select * from user"
result = dal.get_rows(sql)

for item in result:
    print item[0],':',item[1],':',item[2]
