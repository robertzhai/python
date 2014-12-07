# -*- coding:utf-8 -*-

import urllib,urllib2


class HttpClient:
    
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36'
    proxy = ''
    
    def __init__(self):
        urllib2.socket.setdefaulttimeout(8) # timeout
        pass
    
    def set_ua(self,user_agent):
        self.user_agent = user_agent
        
    def set_proxy(self,proxy):
        self.proxy = proxy
        
    def get(self,url,data = {}):
        headers = { 
                        'User-Agent' : self.user_agent,
                        'Referer': 'http://www.cn360cn.com/',
                        'Host':'www.cn360cn.com'
                  }
          
        data = urllib.urlencode(data)
        req = urllib2.Request(url, data, headers)    
        response = urllib2.urlopen(req)    
        response = response.read() 
        return response
    


if __name__ == '__main__':
    c = HttpClient()
    print c.get("http://blog.csdn.net/pleasecallmewhy/article/details/8923067")   
        
        
    
    