'''
Created on 2013-7-19

@author: Administrator
'''
import framework.model.DAO as DAO;

dal = DAO.DAO();

sql="""
create table school(
 id int primary key not null auto_increment,
 name varchar(100),
 city tinyint,
 intro varchar(300)
)default charset=utf8,engine=innodb

"""
result = dal.execute(sql);
print result