import urllib2
import urllib
import socket

socket.setdefaulttimeout(120)

def httppost(url, body=None):
   
    proxy_url = '58.62.43.131:9999'
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

print httppost("http://www.baidu.com")