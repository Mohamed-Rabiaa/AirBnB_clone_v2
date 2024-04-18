#!/usr/bin/python3
""" holds the class User """
import models
from models.base_model import BaseModel, Base
from models.place import Place
from models.review import Review
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """ Representation of the user """

    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    # places = relationship("Place", back_populates="user", cascade="delete")
    # reviews = relationship("Review", back_populates="user", cascade="delete")

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
