'''
Created on 2013-7-27

@author: Administrator
'''
import urllib2
import string

#url="http://proxy.ipcn.org/proxylist.html"
url="http://www.site-digger.com/html/articles/20110516/proxieslist.html"

myPage = urllib2.urlopen(url).read()
print myPage