#-*- coding: utf-8 -*-

'''
Created on 2013-12-21

@author: Administrator
'''
def test5(*args,**kargs):
    print args #输出(1, 2, 3, 4, 5)
    print kargs #输出{'a': 'aa', 'c': 'cc', 'b': 'bb', 'e': 'ee', 'd': 'dd'}
test5(1,2,3,4,5,c='cc',b='bb',a='aa',d='dd',e='ee')

