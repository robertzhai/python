'''
Created on 2013-7-19

@author: Administrator
'''
import framework.model.DAO as DAO;

dal = DAO.DAO();

#sql = "delete from user where id=13";
result = dal.delete({'id':13});
print result