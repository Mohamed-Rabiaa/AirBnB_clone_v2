#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Review(BaseModel, Base):
    """This is the class for Review
    Attributes:
        __tablename__: table name
        place_id: place id
        user_id: user id
        text: review description
    """
    __tablename__ = "reviews"
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)

    '''
    user = relationship(
        "User",
        back_populates="reviews",
        cascade="all, delete")
    '''
    # place = relationship("Place", backref="reviews", cascade="all, delete")
