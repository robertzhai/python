'''
Created on 2013-7-26
  re.I(IGNORECASE): 
   re.M(MULTILINE):
    re.S(DOTALL): 
    re.L(LOCALE): 
    re.U(UNICODE):  
    re.X(VERBOSE): 
@author: Administrator
'''
#encoding=utf-8
import re

pattern = re.compile(r'hello')

match1 = pattern.match('hello job')
match2 = pattern.match('jack hello')
match3 = pattern.match('rrrr hello job hello job')

if match1:
    print match1.group()
else:
    print "match1 fail"
    

if match2:
    print match2.group()
else:
    print "match2 fail"


if match3:
    print match3.group()
else:
    print "match3 fail"
    
match4 = pattern.search('hello job')
match5 = pattern.search('jack hello')
match6 = pattern.search('rrrr hello job hello job')

if match4:
    print match4.group()
else:
    print "match4 fail"
    

if match5:
    print match5.group()
else:
    print "match5 fail"


if match6:
    print match6.group()
else:
    print "match6 fail"
    

