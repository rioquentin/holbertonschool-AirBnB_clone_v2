#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import relationship
from sqlalchemy import ForeignKey, Column, String
from models import type_storage

class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    if type_storage == 'db':
        __tablename__ = 'cities'
        name = Column(String(60), nullable=False)
        state_id = Column(String(128), ForeignKey('states.id'), nullable=False)
        places = relationship(
            "Place",
            backref='cities',
            cascade="all, delete",
            passive_deletes=True)
    else:
        state_id = ""
        name = ""
