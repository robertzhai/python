'''
Created on 2013-7-27

 抓取以下网站的代理服务器
http://proxy.ipcn.org/proxylist.html
http://www.samair.ru/proxy
http://www.proxylists.net
http://www.cz88.net/proxy
http://www.cnproxy.com/
http://www.site-digger.com/html/articles/20110516/proxieslist.html
http://dailifuwuqi.com/freeproxy/20130715/
http://www.cnproxy.com/

@author: Administrator
'''

import framework.model.Url as Url
import framework.model.DAO as DAO;
import framework.model.Proxy as Proxy
import sys


#dal = DAO.DAO();
proxy = Proxy.Proxy()

ips =  Url.Url.fetch_ipcn();
proxy.add_proxy(ips)

ips =  Url.Url.fetch_digger();
proxy.add_proxy(ips)

ips =  Url.Url.fetch_samair();
proxy.add_proxy(ips)

ips =  Url.Url.fetch_proxylists();
proxy.add_proxy(ips)

ips =  Url.Url.fetch_cz88();
proxy.add_proxy(ips)

ips =  Url.Url.fetch_dailifuwuqi();
proxy.add_proxy(ips)