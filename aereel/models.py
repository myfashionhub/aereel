from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from datetime import datetime
from sqlalchemy import Table, Column, Integer, String, DateTime, ForeignKey, \
    UniqueConstraint

Base = declarative_base()

class User(Base):
    __tablename__  = 'users'
    id             = Column(Integer, primary_key=True)
    created_at     = Column(DateTime, default=datetime.utcnow)
    email          = Column(String(256), nullable=False, index=True)
    name           = Column(String(50))
    # __table_args__ = (
    #                   UniqueConstraint('key', 'target_url', 'criteria', name='uq_1'),
    #                  )

class Item(Base):
    __tablename__  = 'items'
    id             = Column(Integer, primary_key=True)
    created_at     = Column(DateTime, default=datetime.utcnow)
    title          = Column(String(256))
    description    = Column(String(1024))
    categories     = Column(String(256))

class Category(Base):
    __tablename__  = 'categories'
    id             = Column(Integer, primary_key=True)
    created_at     = Column(DateTime, default=datetime.utcnow)
    name           = Column(String(256))

class Save(Base):
    __tablename__  = 'saves'
    id             = Column(Integer, primary_key=True)
    created_at     = Column(DateTime, default=datetime.utcnow)
    item_id        = Column(Integer, ForeignKey('items.id'))
    user_id        = Column(Integer, ForeignKey('users.id'))
