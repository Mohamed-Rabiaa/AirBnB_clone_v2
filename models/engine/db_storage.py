#!/usr/bin/python3
""" This module contains the DBStorage class """


from sqlalchemy import (create_engine)


class DBStorage():
    """ DBStorage class """
    __engine = None
    __session = None

    def __init__(self):
        """ This method creates the engine of the instance """
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}' .format(
