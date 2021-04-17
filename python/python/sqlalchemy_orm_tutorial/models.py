"""
..https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_orm_declaring_mapping.htm
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Customers(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True)

    name = Column(String)
    address = Column(String)
    email = Column(String)
