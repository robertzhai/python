# -*- coding:utf-8 -*-

from selenium import webdriver

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

driver = webdriver.PhantomJS(executable_path='/usr/local/bin/phantomjs')  # 这要可能需要制定phatomjs可执行文件的位置
driver.get("http://www.ip.cn/125.95.26.81")
# print driver.current_url
# print driver.page_source
print driver.find_element_by_id('result').text.split('\n')[0].split('来自：')[1]
driver.quit