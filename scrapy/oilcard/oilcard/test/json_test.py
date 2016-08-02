# -*- coding: utf-8 -*-
import json

# json_data = '{"name": "Brian", "city": "Seattle"}'
# # print json_data['name']
# python_obj = json.loads(json_data)
# print python_obj["name"]
# print python_obj["city"]

json_data = {'amount': u'15000',
 'balance': u'282606',
 'litre': u'2370',
 'nodeTag': u'\u6ee8\u5dde\u77f3\u6cb9\u7b2c5\u52a0\u6cb9\u7ad9',
 'oilName': u'95\u53f7\u8f66\u7528\u6c7d\u6cb9(V)',
 'opeTime': u'2016-07-30 17:59:44',
 'price': u'633',
 'reward': u'0',
 'traName': u'\u52a0\u6cb9'}


python_obj = json.loads(json_data)
print python_obj["amount"]