'''
Created on 2013-7-20

@author: Administrator
'''
import framework.config.mysql as db;

print db.conf['host'];

class A:
    @staticmethod
    def aa():
        print "static method"
        


A.aa()

