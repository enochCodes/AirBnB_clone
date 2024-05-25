# models/base_model.py

from datetime import datetime
from models.engine.file_storage import FileStorage
import uuid

class BaseModel:
    def __init__(self, *args, **kwargs):
        # Delayed import
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
            storage = FileStorage()
            storage.new(self)

    def save(self):
        """Update `updated_at` timestamp and save object."""
        # Delayed import
        self.updated_at = datetime.now()
        storage = FileStorage()
        storage.save()

    def reload(self):
        # Delayed import
        storage = FileStorage()
        storage.reload()

    def to_dict(self):
        """ To dict """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
