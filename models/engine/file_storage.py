#!/usr/bin/python3
"""
This module contains the class FileStorage
"""
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import json
import os


class FileStorage:
    """
    FileStorage class
    """
    __file_path = "file.json"
    __object = {}

    def all(self):
        """Returns all objects from the dictionary __objects"""
        return self.__object

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        self.__object["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, "w", encoding="UTF-8") as f:
            obj_dict = {k: v.to_dict() for k, v in self.__object.items()}
            json.dump(obj_dict, f)

    def reload(self):
        """deserializes the JSON file to __objects, only if the JSON
        file (__file_path) exists. Otherwise, do nothing.
        """
        classes = {
                "BaseModel": BaseModel,
                "User": User,
                "State": State,
                "City": City,
                "Amenity": Amenity,
                "Place": Place,
                "Review": Review
                }
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r", encoding="UTF-8") as f:
                obj_dict = json.load(f)
                for k, v in obj_dict.items():
                    name = k.split('.')[0]
                    if name in classes:
                        obj = classes[name](**v)
                    self.__class__.__object[k] = obj
