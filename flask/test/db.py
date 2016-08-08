# -*- coding: utf-8 -*-
from sqlalchemy import Column, String, create_engine, Integer, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class Entries(Base):
    # 表的名字:
    __tablename__ = 'flask_entries'

    # 表的结构:
    id = Column(Integer, primary_key=True)
    title = Column(Text)
    text = Column(Text)


# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://test:test@localhost:3306/python')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
print DBSession

# 创建session对象:
session = DBSession()
data = session.query(Entries).all()
print repr(data)
for obj in data:
    print obj.id,obj.title,obj.text
