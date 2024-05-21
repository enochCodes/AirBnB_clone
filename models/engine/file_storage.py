#!/usr/bin/python3
"""
    file storage json
"""
# models/file_storage.py
from models.base_model import BaseModel
import json
from datetime import datetime


class FileStorage:
    """Handles storage of all models in the application."""
    __objects = {}
    __file_path = "file.json"

    def __init__(self):
        pass

    def all(self):
        return self.__objects

    def new(self, obj):
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """Serializes the objects to the JSON file."""
        with open(self.__file_path, 'w') as file:
            json.dump(
                    {k: v.to_dict() for k,
                        v in self.__objects.items()},
                    file
                    )

    def reload(self):
        """Deserialize the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                obj_dict = json.load(f)
            for key, value in obj_dict.items():
                cls = value["__class__"]
                self.__objects[key] = eval(cls)(**value)
        except FileNotFoundError:
            pass