#!/usr/bin/python3

"""Defines the BaseModel class."""
import json
from models.base_model import BaseModel

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects
    
    def new(self, obj):
        """Sets in __objects the obj with key <obj_class_name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(new_dict, f)

    def reload(self):
        try:
            with open(FileStorage.__file_path, "r") as f:
                obj_dict = json.load(f)
            for key, value in obj_dict.items():
                class_name = value["__class__"]
                FileStorage.__objects[key] = eval(class_name)(**value)
        except FileNotFoundError:
            pass