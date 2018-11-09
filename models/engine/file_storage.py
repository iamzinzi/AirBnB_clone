#!/usr/bin/python3
"""
This module contains the class FileStorage
"""
#from models.base_model import BaseModel
import models
import json
import os


class FileStorage:
    """
    FileStorage class
    """
    __file_path = "file.json"
    __object = {}

    def all(self):
        return self.__object

    def new(self, obj):
        self.__object["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        with open(self.__file_path, "w", encoding="UTF-8") as f:
            obj_dict = {k: v.to_dict() for k, v in self.__object.items()}
            f.write(json.dumps(obj_dict))
    def reload(self):
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r", encoding="UTF-8") as f:
                obj_dict = json.loads(f.read())
                for k, v in obj_dict.items():
                    #obj = BaseModel(**v) 
                    #print(obj.to_dict())
                    #self.__object[k] = obj
                    print("lol")
