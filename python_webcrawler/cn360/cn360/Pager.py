# -*_ coding: utf-8 -*-
'''
Created on 2013-12-21

@author: Administrator
'''
import HttpClient
import re
import Dao

class Pager:
    
    client = ''
    dao = ''
    def __init__(self):
        self.client = HttpClient.HttpClient()
        self.dao = Dao.Mysql()
        
        pass
    
    def get_html(self,url):
        html = self.client.get(url)
        #gb2312 to unicode to utf8
        html = html.decode('gb2312', 'ignore').encode('utf-8')
#        print html
        self.parse_html(html)
     

    def parse_html(self,html):
        page_pattern = re.compile(r'<li>\s*<a.*?>(.*?)<\/a>\s*<div\s+class=tel\s*>\s*电话:(.*?)地址:(.*?)<\/div>\s*<\/li>', re.I | re.M)
#        page_pattern = re.compile(r'<li>\s*<a.*?>(.*?)<\/a>\s*<div\s+class=tel\s*>\s*(.*?)<\/div>\s*<\/li>', re.I | re.M)
        result =  page_pattern.findall(html)
        for item in result:
#            print item[0],',',item[1],',',item[2]
            tag, number, address = item[0],item[1],item[2]
            number = number.strip()
            number = number.replace("-", "")
            tag = tag.strip()
            address = address.strip()
            temp = {'tag':tag,'number':number,'address':address}
            result = self.dao.insert(temp)
            
        
 
if __name__ == '__main__':
    page = Pager()
    url = 'http://www.cn360cn.com/news.aspx?pageno=2'
    page.get_html(url)   