'''
Created on 2013-7-26
sub(repl, string[, count]) | re.sub(pattern, repl, string[, count]):
@author: Administrator
'''
import re

p = re.compile(r'(\w+) (\w+)')
s = 'i say , hello world'

print p.sub(r'', s)

def func(m):
    return m.group(1).title() + ' ' + m.group(2).title()

print p.sub(func, s)


