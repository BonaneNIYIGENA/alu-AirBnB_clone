#!/usr/bin/python3
"""Module for FileStorage class"""
import json
from models.base_model import BaseModel


class FileStorage:
    """Serializes instances to JSON and deserializes JSON to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(new_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, "r") as f:
                obj_dict = json.load(f)
            for key, val in obj_dict.items():
                cls_name = val["__class__"]
                FileStorage.__objects[key] = eval(cls_name)(**val)
        except FileNotFoundError:
            pass
