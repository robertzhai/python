'''
Created on 2013-7-20

@author: Administrator
'''
import urllib
import urllib2

class Url(object):
    
    @staticmethod
    def get_content(url, proxy = None):
        content = urllib2.urlopen(url).read()
        return content


def httppost(url, body=None):
    proxy_url = '220.11.11.11';#get_proxy_online()
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

#print Url.get_content('http://proxy.ipcn.org/proxylist.html');

req = urllib2.Request('http://proxy.ipcn.org/proxylist.html')
req.add_header('Referer', 'http://www.python.org/')
r = urllib2.urlopen(req)
print r
