#!/usr/bin/python3
""" This module contains the DBStorage class """


from sqlalchemy import (create_engine)
from os import getenv
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage():
    """ DBStorage class """
    __engine = None
    __session = None

    def __init__(self):
        """ This method creates the engine of the instance """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB'),
                                              pool_pre_ping=True))
        Base.metadata.create_all(self.__engine)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(engine)

    def all(self, cls=None):
        """ all method """
        obj_dct = {}
        if (cls):
            query = self.__session.query(cls).all()
            for obj in query:
                key = "{}.{}".format(cls.__name__, obj.id)
                obj_dct[key] = obj

        else:
            cls_lst = [User, State, City, Amenity, Place, Review]
            for c in cls_lst:
                query = self.__session.query(c).all()
                for obj in query:
                    key = "{}.{}".format(c.__name__, obj.id)
                    obj_dct[key] = obj

        return obj_dct

    def new(self, obj):
        """ add the object to the current database session """
        if obj:
            self.__session.add(obj)

    def save(self):
        """ commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from the current database session obj if not None """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ creates all tables in the database
        and creates the current database session """
        Base.metadata.create_all(self.__engine)
        self.__session = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(self.__session)
        self.__session = Session()
