# -*- coding: utf-8 -*-
import urllib2
import re
import sys
import chardet

reload(sys)                      # reload 才能调用 setdefaultencoding 方法
sys.setdefaultencoding('utf-8')  # 设置 'utf-8'

url = 'http://tianqi.2345.com/js/citySelectData.js'
req = urllib2.Request(url)
content = urllib2.urlopen(req).read()
content = content.decode('gbk').encode('utf-8')
# print content;


fh = open('city.txt')

codes = {}
while True:
    line = fh.readline()
    if not line:
        break

    city = line.strip('\n')
    print city

    pattern = re.compile(r'\S+-[0-9]{4,}')
    match = pattern.findall(content)
    unicode_city = city.decode('utf-8')
    for text in match:
        if text:
            text = text.split('-')
            if text[0] == unicode_city:
                print text, text[0],text[1]
                codes[text[1]] = text[0].encode('utf-8')

print codes
fh.close()


fh = open('code_city.txt', 'w')
for (k,v) in codes.iteritems():
    print k,v
    fh.write(k + ',' + v + '\n')
print len(codes)

fh.close()
