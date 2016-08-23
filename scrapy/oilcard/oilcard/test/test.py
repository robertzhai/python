# -*- coding: utf-8 -*-

import json

json_data = '{"holders":"刘林","no":"1000113700015701707","list":[]}';
python_obj = json.loads(json_data)

if 'list' in python_obj and python_obj['list']:
    print python_obj['list']
else:
    print '---'
    python_obj['list']
    print '---'
    print 'list empty'
# print python_obj["amount"],python_obj['list']

fo = open("/wwwroot/scrapy/oilcard/log.txt", "a+")
fo.write("billQueryAction_transactionLog.json result:11\n");
# 关闭打开的文件
fo.close()
