# -*- coding: utf-8 -*-

from sqlalchemy import Column, String, create_engine, Integer, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 定义Entry对象:
class Entry(Base):
    # 表的名字:
    __tablename__ = 'flask_entries'

    # 表的结构:
    id = Column(Integer, primary_key=True)
    title = Column(Text)
    text = Column(Text)