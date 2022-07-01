#!/usr/bin/python3
"""
Class FileStorage
"""

import json
import os
from models.base_model import BaseModel


class FileStorage:
    """
    Class that serializes instances to a JSON file
    and deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """

        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """

        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path)
        """

        obj_dict = {}
        for key, value in FileStorage.__objects.items():
            obj_dict[key] = FileStorage.__objects[key].to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists;
        otherwise, do nothing.
        """

        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                dict_obj = json.load(file)
                for key, value in dict_obj.items():
                    FileStorage.__objects[key] =\
                         eval(value["__class__"])(**value)
        except Exception:
            pass
