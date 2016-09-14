# -*- coding: utf-8 -*-
#!/root/.jumbo/bin/python

import json
import time
import cPickle
import numpy as np
import lib.feature_utils

from util.CouponForm import CouponForm

from flask import Flask, request

from lib.Predict import Predict

app = Flask(__name__)
predict = Predict()

@app.route('/')
def index():
    return 'hello machine learning'

@app.route('/coupon')
def coupon():
    data = {'amount':10, 'time':int(time.time())}
    result = {'errno':0, 'errstr':'','data':data}
    return json.dumps(result) 


@app.route('/getcoupon', methods=['POST'])
def getcoupon():

    data = {'amount':0}
    try:

        coupon_form = CouponForm(request.form, csrf_enabled=False)
        if not coupon_form.validate_on_submit():
            field, errors = coupon_form.errors.items()[0]
            raise Exception(errors[0])

        order = {}
        order['pid'] = int(coupon_form.data['pid'])
        order['coupon_amount'] = int(coupon_form.data['coupon_amount'])
        order['pay_amount'] = int(coupon_form.data['pay_amount'])
        #获取预测结果
        amount = predict.predict(**order)
        data['amount'] = amount
        result = {'errno': 0, 'errstr': '', 'data': data}
    except Exception as e:
        result = {'errno': 1001, 'errstr': e.message}

    return json.dumps(result) 


if __name__ == '__main__':
   app.run()
