#!/usr/bin/python3
"""
    Base Model
"""
# models/base_model.py

from models.engine.file_storage import FileStorage
from datetime import datetime
import uuid

storage = FileStorage()


class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
            self.created_at = datetime.strptime(
                    kwargs['created_at'],
                    '%Y-%m-%dT%H:%M:%S.%f'
                    )
            self.updated_at = datetime.strptime(
                    kwargs['updated_at'],
                    '%Y-%m-%dT%H:%M:%S.%f'
                    )
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def save(self):
        """Update `updated_at` timestamp and save object."""
        self.updated_at = datetime.now()
        storage = FileStorage()
        storage.save(self)  # Ensure storage object is used
    
    def reload(self):
        from models.engine.file_storage import FileStorage
        storage = FileStorage()
        storage.reload()

    def to_dict(self):
        """ To dict """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
