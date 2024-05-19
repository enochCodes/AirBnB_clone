#!/usr/bin/python3
"""
    file storage json
"""
# models/file_storage.py

import json

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
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, file)

    def reload(self):
        """Deserializes the JSON file to objects."""
        try:
            with open(self.__file_path, 'r') as file:
                self.__objects = json.load(file)
                for key, value in self.__objects.items():
                    cls = value["__class__"]
                    self.__objects[key] = eval(cls)(**value)
        except FileNotFoundError:
            pass
