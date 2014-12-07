'''
Created on 2013-7-26
finditer(string[, pos[, endpos]]) | re.finditer(pattern, string[, flags]):

@author: Administrator
'''
#encoding=utf-8
import re

p = re.compile(r'\d+')

for m in p.finditer('one1two2three3'):
    print m.group()