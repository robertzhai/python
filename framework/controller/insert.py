'''
Created on 2013-7-20

@author: Administrator
'''
import framework.model.DAO as DAO;

dal = DAO.DAO();

data = {'name':'robert','age':1216}
result = dal.insert(data);
print result