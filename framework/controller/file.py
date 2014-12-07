'''
Created on 2013-7-21

@author: Administrator
'''

import framework.tool.FileHandler as FileHandler
import os,sys

fh = FileHandler.FileHandler("../data/num.txt")
print fh.read_lines()

print os.getcwd();

print fh.scan_dir(os.getcwd())

fh.close()

