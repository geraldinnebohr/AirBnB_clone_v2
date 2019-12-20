#!/usr/bin/python3
"""
=============================
Saving data in Mysql database
=============================
"""

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
import os
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """class for save data"""

    __engine = None
    __session = None

    def __init__(self):
        """The constructor"""

        USER = os.getenv('HBNB_MYSQL_USER')
        PWD = os.getenv('HBNB_MYSQL_PWD')
        HOST = os.getenv('HBNB_MYSQL_HOST')
        DB = os.getenv('HBNB_MYSQL_DB')
        ENV1 = os.getenv('HBNB_ENV')
        STORAGE = os.getenv('HBNB_TYPE_STORAGE')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'
                                      .format(USER, PWD, HOST, DB),
                                      pool_pre_ping=True)

        if ENV1 == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session

       clas_list = [State, City, User, Place]
        query = []
        if cls is None:
            for yo in clas_list:
                query.append(self.__session.query(yo).all())
            another_list = [x for sublist in query for x in sublist]
        else:
            another_list = self.__session.query(cls).all()
        my_dict = {}
        for ki in another_list:
            la_ki = ki.to_dict()['__class__'] + "." + getattr(ki, 'id')
            my_dict[la_ki] = ki
        return my_dict
"""
        my_dict = {}
        if cls:
            query = self.__session.query(cls)
            for obj in query:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                my_dict[key] = obj
        else:
            lista = [State, City, User]
            for _class in lista:
                query = self.__session.query(_class)
                for obj in query:
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    my_dict[key] = obj
        return my_dict

    def new(self, obj):
        """add object to the current database session"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """commit all changes of the session"""

        self.__session.commit()

    def delete(self, obj=None):
        """delete obj from the session"""

        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create tables in the database and create the session"""

        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        session = scoped_session(Session)
        self.__session = session()
