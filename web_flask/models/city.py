#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ This is the class for City Attributes:
        __tablename__: name of the table represented
        state_id: The state id
        name: input name
    """

    __tablename__ = "cities"
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
    # state = relationship("State", backref="cities", cascade="all, delete")
    places = relationship("Place", cascade="all, delete", backref="cities")
