#!/usr/bin/python3
"""
    Base Model
"""

import uuid
from datetime import datetime
import FileStorage as storage

class BaseModel:
    """Base Model class"""
    def __init__(self, *args, **kwargs):
        """ Init atrr """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.fromisoformat(value))
                elif key != '__class__':
                    setattr(self, key, value)
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            if 'created_at' not in kwargs:
                self.created_at = datetime.now()
            if 'updated_at' not in kwargs:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """ Str atrr """
        return "[{}] ({}) {}".format(
                self.__class__.__name__,
                self.id, self.__dict__
                )

    def save(self):
        """ save """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ To dict """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
