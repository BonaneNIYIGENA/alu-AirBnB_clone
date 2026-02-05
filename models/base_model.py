#!/usr/bin/python3
"""Module for BaseModel Class"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """Defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Initializes the instance"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Returns string representation of the instance"""
        cls_name = self.__class__.__name__
        return "[{}] ({}) {}".format(cls_name, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__"""
        res_dict = self.__dict__.copy()
        res_dict['__class__'] = self.__class__.__name__
        res_dict['created_at'] = self.created_at.isoformat()
        res_dict['updated_at'] = self.updated_at.isoformat()
        return res_dict