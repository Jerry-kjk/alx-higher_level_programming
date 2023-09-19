#!/usr/bin/python3
"""
Contains the class definition of a State and an instance declarative_base().
"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Class with id and name attributes of each state.
    """
    __tablename__ = 'states'

    id = Column(Integer, autoincrement=True, unique=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
