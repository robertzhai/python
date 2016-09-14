# -*- coding: utf-8 -*-
from flask_wtf import Form
from wtforms import IntegerField,StringField
from wtforms.validators import DataRequired,Regexp

class CouponForm(Form):


    pid = StringField('pid', validators=[ DataRequired(), Regexp(r'^\d+$',
               message='pid param error')])
    coupon_amount = StringField('coupon_amount', validators=[ DataRequired(), Regexp(r'^\d+$',
               message='coupon_amount param error')])
    pay_amount = StringField('pay_amount', validators=[ DataRequired(), Regexp(r'^\d+$',
               message='pay_amount param error')])
    # coupon_amount = IntegerField('coupon_amount', validators=[DataRequired()])
    # pay_amount = IntegerField('pay_amount', validators=[DataRequired()])
    # password = PasswordField(u'密码', validators=[Required(), Length(6, 12, message=u'密码长度在6到12为')])
    # password1 = PasswordField(u'确认密码', validators=[Required(), Length(6, 12, message=u'密码长度在6到12为'), EqualTo('password', message=u'密码必须一致')])
    # verification_code = StringField(u'验证码', validators=[Required(), Length(4, 4, message=u'填写4位验证码')])
    # submit = SubmitField(u'注册')