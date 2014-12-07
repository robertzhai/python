'''
Created on 2013-7-21

@author: Administrator
'''

import os

class FileHandler(object):
    
    def __init__(self, filename , mode = "r"):
        self.handle = open(filename, mode)
    
    def close(self):
        self.handle.close()
        
    def read_one_line(self):
        return self.handle.readline()
    
    def read_lines(self):
        return self.handle.readlines()
    
    def seek(self, pos):
        self.handle.seek(pos)
        
    def tell(self):
        return self.handle.tell()
    
    def makedir(self,dirname):
        os.mkdir(dirname)
        
    def remove_file(self,filename):
        os.remove(filename)
        
    @staticmethod
    def scan_dir(dirname):
        
        if not dirname:
            return False
        
        files = [];
        for item in os.listdir(dirname):
            files.append(dirname + "/" + item)
        return files
    
    def file_put_contents(self, content):
        self.handle.write(content)
    
    
        
        
    