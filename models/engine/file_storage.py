#!/usr/bin/python3
"""
    file storage json
"""
import json


class FileStorage:
    """Storage JSON dump"""
    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects = append(obj)
        

    def save(self):
        """Serilalizes the Objects the obj with key"""
        __file_path = json.dumps(__objects)

    def reload(self):
        """
            Deserializers the JSON file to Objects
            (only if the JSON file (__file_path)
        """
        __objects = json.loads(__file_path)
