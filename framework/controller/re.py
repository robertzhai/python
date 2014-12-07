'''
Created on 2013-8-4

@author: Administrator
'''
import re

s = 'This and that'
print s

print re.finditer(r'(th\w+) and (th\w+)', s, re.I).next().groups()
