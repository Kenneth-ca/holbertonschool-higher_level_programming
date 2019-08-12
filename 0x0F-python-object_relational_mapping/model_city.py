#!/usr/bin/python3
"""
A python file that contains the class definition of a State
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base

class City(Base):
    """
    Class definition of City
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
