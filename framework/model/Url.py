'''
Created on 2013-7-27

@author: Administrator
'''
import re
import urllib2
import string
import urllib
import sys
import time

class Url(object):
    
    @staticmethod
    def get_file(url, proxy):
        if proxy:
            return Url.get_file_by_proxy(url, proxy)
        return urllib2.urlopen(url).read()
    
    @staticmethod
    def get_file_by_proxy(url, proxy_url, body=None):
#        proxy_url = '58.62.43.131:9999'
        proxy_support = urllib2.ProxyHandler ( { 'http' : proxy_url } ) 
        opener=urllib2.build_opener(proxy_support, urllib2.HTTPHandler)
        opener.addheaders=[('User-agent','Mozilla/4.0(compatible;MSIE6.0;WindowsNT5.1)')]
        urllib2.install_opener(opener)
    
        if body :
            req=urllib2.Request(url, urllib.urlencode(body))
        else :
            req=urllib2.Request(url)
        u=urllib2.urlopen(req)
        return u.read()
    
    
    @staticmethod
    def fetch_ipcn(proxy = None):
        url = "http://proxy.ipcn.org/proxylist.html"
        html = Url.get_file(url, proxy)
        re_obj = re.compile("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,8}", re.S | re.M)
        result = re_obj.findall(html)
        return result
    
    @staticmethod
    def fetch_digger(proxy = None):
        url = "http://www.site-digger.com/html/articles/20110516/proxieslist.html";
        html = Url.get_file(url, proxy)
        print html
        re_obj = re.compile("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,8}", re.S | re.M)
        result = re_obj.findall(html)
        return result
    
    @staticmethod
    def fetch_samair(proxy = None):
        ips = [];
        for i in range(1,11):
            url = "http://www.samair.ru/proxy/proxy-%02d.htm" % (i)
            html = Url.get_file(url, proxy)
            re_obj = re.compile("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,8}", re.S | re.M)
            result = re_obj.findall(html)
            ips += result
        
        return ips
    
    @staticmethod
    def fetch_proxylists(proxy = None):
        url = "http://www.proxylists.net/http_highanon.txt";
        html = Url.get_file(url, proxy)
        print html
        re_obj = re.compile("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,8}", re.S | re.M)
        result = re_obj.findall(html)
        return result
     
    @staticmethod
    def fetch_cz88(proxy = None):
        ips = [];
        for i in range(1,11):
            if i == 1:
                url = "http://www.cz88.net/proxy/index.aspx"
            else :
                url = "http://www.cz88.net/proxy/http_%d.aspx" %(i)
            
            html = Url.get_file(url, proxy)
            re_obj = re.compile("<td>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})<\/td>\s*<td>(\d{1,8})<\/td>", re.S | re.M)
            result = re_obj.findall(html)
            ips += result
        
        result = []
        for item in ips:
            result.append(item[0] + ":" + item[1])
            
        return result
    
    @staticmethod
    def fetch_dailifuwuqi(proxy = None):
         url = "http://dailifuwuqi.com/freeproxy/" + time.strftime("%Y%m%d") + "/"
         html = Url.get_file(url, proxy)
         print html
         re_obj = re.compile("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s*:\s*\d{1,8}", re.S | re.M)
         result = re_obj.findall(html)
         
         ips = []
         for item in result:
             ips.append(item.replace(" ",""))
         
         return ips
     
    @staticmethod
    def fetch_proxy_com(proxy = None):
         
        ips = []
         
        for i in range(1, 11):
            url = "http://www.cnproxy.com/proxy%d.html" % (i)
            html = Url.get_file(url, proxy)
        print html
  
    