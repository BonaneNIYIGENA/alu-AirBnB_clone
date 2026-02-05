#!/usr/bin/python3

"""Defines the BaseModel class."""
import uuid
from datetime import datetime
import models

class BaseModel:
    """Represents the BaseModel of the AirBnB clone project."""
    def __init__(self, *args, **kwargs):
        """Initializes a new BaseModel instance."""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
 
        models.storage.new(self)

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of the instance."""
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return my_dict