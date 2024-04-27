#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, Table, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
import models


if getenv("HBNB_TYPE_STORAGE") == "db":
    place_amenity = Table(
        'place_amenity',
        Base.metadata,
        Column(
            'place_id',
            String(60),
            ForeignKey("places.id"),
            primary_key=True,
            nullable=False),
        Column(
            'amenity_id',
            String(60),
            ForeignKey("amenities.id"),
            primary_key=True,
            nullable=False))


class Place(BaseModel, Base):
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    # user = relationship("User", backref="places", cascade="delete")
    # cities = relationship("City", backref="places", cascade="all, delete")
    amenity_ids = []

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship("Review", backref="place",
                               cascade="all, delete-orphan")
        amenities = relationship(
            "Amenity",
            secondary='place_amenity',
            backref="places",
            viewonly=False)

    else:
        @property
        def reviews(self):
            """get all refiews with the current place id
            from filestorage
            """
            list = [
                v for k, v in models.storage.all(models.Review).items()
                if v.place_id == self.id
            ]
            return list

        @property
        def amenities(self):
            """get all amenities with the current place id
            """
            list = [
                v for k, v in models.storage.all(models.Amenity).items()
                if v.id in self.amenity_ids
            ]
            return list

        @amenities.setter
        def amenities(self, obj):
            """ handles append method for adding an Amenity.id to
            the attribute amenity_ids """
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)
