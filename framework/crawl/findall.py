'''
Created on 2013-7-26

@author: Administrator
'''
import re

p = re.compile(r'\d+')
print p.findall('one1two2three3four4')