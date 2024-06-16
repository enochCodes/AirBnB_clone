#!/usr/bin/python3
import unittest
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    
    def setUp(self):
        """Set up test methods with the initial conditions needed."""
        FileStorage._FileStorage__objects = {}
        storage.reload()

    def test_all_method(self):
        """Test that all method retrieves stored objects."""
        all_objs = storage.all()
        self.assertIsInstance(all_objs, dict)

    def test_create_new_object(self):
        """Test creation of a new BaseModel object."""
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model.save()
        retrieved_objects = storage.all()
        object_key = f'BaseModel.{my_model.id}'
        self.assertIn(object_key, retrieved_objects)

if __name__ == "__main__":
    unittest.main()
