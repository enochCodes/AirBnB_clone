#!/usr/bin/python3

import os
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
# tests/test_models/test_engine.py

class test_file_storage(unittest.TestCase):

    def setUp(self):
        """Set up initial conditions for tests."""
        self.storage = FileStorage()
        self.obj = BaseModel()
        self.obj.name = "Test Model"
        self.obj.my_number = 100
        self.file_path = FileStorage._FileStorage__file_path
        FileStorage._FileStorage__objects = {}

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

if __name__ == '__main__':
    unittest.main()
