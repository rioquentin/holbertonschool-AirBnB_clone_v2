#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, Column, String
from models import storage
from os import getenv
from models.city import City

class State(BaseModel):
    """ State class """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'state'
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        cities = relationship(
            "City",
            backref="state",
            cascade="delete",
            )
    else:
        name = ""

        @property
        def cities(self):
            "getter cities"
            list_cities = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    list_cities.append(city)
            return list_cities
