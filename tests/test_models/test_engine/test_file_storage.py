#!/usr/bin/python3
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import *
from models.engine.file_storage import FileStorage
import unittest
import os
# tests/test_models/test_engine.py

class TestFileStorage(unittest.TestCase):

    def setUp(self):
        """Set up initial conditions for tests."""
        self.storage = FileStorage()
        self.obj = BaseModel()
        self.obj.name = "Test Model"
        self.obj.my_number = 100
        self.file_path = FileStorage._FileStorage__file_path
        FileStorage._FileStorage__objects = {}
        storage.reload()

    def tearDown(self):
        """Clean up after each test."""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        FileStorage._FileStorage__objects = {}

    def test_all_method(self):
        """Test that all method retrieves stored objects."""
        # Ensure the storage starts empty
        self.assertEqual(len(self.storage.all()), 0)
        self.storage.new(self.obj)
        self.assertEqual(len(self.storage.all()), 1)
        all_objs = self.storage.all()
        obj_key = f'BaseModel.{self.obj.id}'
        self.assertIn(obj_key, all_objs)
        self.assertEqual(self.obj, all_objs[obj_key])

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
        
    def test_Save(self):
        print("-- Create a new object --")
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model.save()
        print(my_model)
    
    def test_relod(self):
        all_objs = storage.all()
        print("-- Reloaded objects --")
        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]
            print(obj)
        
        

if __name__ == '__main__':
    unittest.main()
