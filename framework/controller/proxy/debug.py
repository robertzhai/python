'''
Created on 2013-7-27

@author: Administrator
'''
import framework.model.Url as Url
import framework.model.DAO as DAO;
import framework.model.Proxy as Proxy
import sys


#dal = DAO.DAO();
proxy = Proxy.Proxy()
print proxy
#sys.exit()
ips =  Url.Url.fetch_dailifuwuqi();
print ips;
proxy.add_proxy(ips)
    