#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
import models
from models.city import City


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete, delete-orphan",
                          backref='state')

    @property
    def cities(self):
        """method that returns the cities"""

        otro_dict = models.storage.all(City)
        otra_lista = []
        for cositas, otras_cositas in otro_dict.items():
            if otras_cositas.state_id == self.id:
                otra_lista.append(otras_cositas)
        return otra_lista
