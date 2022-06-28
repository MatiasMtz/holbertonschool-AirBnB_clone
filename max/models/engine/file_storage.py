#!/usr/bin/python3
"""

"""

import json
import os
from models.base_model import BaseModel

class FileStorage:
    """
    
    """
    __file_path = "file.json"
    __objects = {}
    def all(self):
        """
        
        """
        return FileStorage.__objects
    
    def new(self, obj):
        """
        
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """

        """
        obj_dict = {}
        for key, value in FileStorage.__objects.items():
            obj_dict[key] = FileStorage.__objects[key].to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_dict, file)
    
    def reload(self):
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                dict_obj = json.load(file)
                for key, value in dict_obj.items():
                    FileStorage.__objects[key] = eval(value["__class__"])(**value)
        except Exception:
            pass
        """
        if os.path.isfile(FileStorage.__file_path) is True:
            with open(FileStorage.__file_path, 'r+', encoding='utf-8') as f:
                obj = json.load(f)
                for key, value in obj.items():
                    FileStorage.__objects[key] = eval(value['__class__'])(**value)
        """