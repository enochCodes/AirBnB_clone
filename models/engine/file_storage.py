#!/usr/bin/python3
"""
    models/engine/file_storage.py
"""
import json

class FileStorage:
    """Handles storage of all models in the application."""
    __objects = {}
    __file_path = "file.json"

    def all(self):
        """Return all objects."""
        return self.__objects

    def new(self, obj):
        """Add new object to storage dictionary."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialize objects to the JSON file."""
        with open(self.__file_path, 'w') as file:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, file)

    def reload(self):
        """Deserialize the JSON file to __objects."""
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    cls_name = value.pop("__class__", None)
                    if cls_name and cls_name in globals():
                        cls = globals()[cls_name]
                        self.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass