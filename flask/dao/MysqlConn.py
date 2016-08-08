# -*- coding: utf-8 -*-
import os
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from config.ConfMysql import ConfMysql

def get_db():
    # engine = create_engine('mysql+mysqlconnector://test:test@localhost:3306/python')
    engine = create_engine(
        ConfMysql['driver'] + '://' + ConfMysql['db_user'] + ':' + ConfMysql['db_password'] +
        '@' + ConfMysql['host'] + ':' + ConfMysql['port'] + '/' + ConfMysql['db']
    )
    # 创建DBSession类型:
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    return session