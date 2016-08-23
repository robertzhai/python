# -*- coding: utf-8 -*-
from selenium import webdriver
import time
driver = webdriver.PhantomJS(executable_path='/usr/local/bin/phantomjs')
driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
time.sleep(3)
print(driver.find_element_by_id("content").text)
driver.close()