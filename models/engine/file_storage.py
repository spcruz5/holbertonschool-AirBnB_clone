#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json

from models.base_model import BaseModel


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
      #string-path to JSON file
    __file_path = 'file.json'
      #dictionary-empty but will store all objects 
    __objects = {}

    def all(self):
        """Returns a dictionary of models currently in storage"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects to obj with key"""
        class_name = type(obj).__name__
        key_obj = "{}.{}".format(class_name, obj.id)
        self.__objects[key_obj] = obj

    def save(self):
        """Serializes __objects to JSON file"""
        firstobj = self.__objects
        objdict = {obj: firstobj[obj].to_dict() for obj in firstobj.keys()}
        with open(self.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r', encoding="UTF8") as f:
                obj_dir = json.loads(f.read())
                for key, value in obj_dir.items():
                    self.__objects[key] = BaseModel(**value)
        except:
            pass
