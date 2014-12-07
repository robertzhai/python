'''
Created on 2013-7-19

@author: Administrator
'''
import framework.model.DAO as DAO;

dal = DAO.DAO();

#sql = "update  user set name='update name' where id= 10";
result = dal.update({'name':'update name'},{'id':12});
print result