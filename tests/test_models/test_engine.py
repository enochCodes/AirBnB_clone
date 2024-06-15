#!/usr/bin/python3

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import unittest
import os
import json

class TestFileStorage(unittest.TestCase):

    def setUp(self):
        """Set up initial conditions for tests."""
        self.storage = FileStorage()
        self.obj = BaseModel()
        self.obj.name = "Test Model"
        self.obj.my_number = 100
        self.file_path = FileStorage._FileStorage__file_path

    def tearDown(self):
        """Clean up after each test."""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

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

    def test_new_method(self):
        """Test that new method stores an object."""
        self.storage.new(self.obj)
        obj_key = f'BaseModel.{self.obj.id}'
        self.assertIn(obj_key, self.storage.all())

    def test_save_method(self):
        """Test that save method serializes objects to JSON file."""
        self.storage.new(self.obj)
        self.storage.save()
        self.assertTrue(os.path.exists(self.file_path))
        with open(self.file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            obj_key = f'BaseModel.{self.obj.id}'
            self.assertIn(obj_key, data)
            self.assertEqual(self.obj.id, data[obj_key]['id'])

    def test_reload_method(self):
        """Test that reload method deserializes JSON file to objects."""
        self.storage.new(self.obj)
        self.storage.save()
        reloaded_storage = FileStorage()
        reloaded_storage.reload()
        obj_key = f'BaseModel.{self.obj.id}'
        self.assertIn(obj_key, reloaded_storage.all())
        reloaded_obj = reloaded_storage.all()[obj_key]
        self.assertEqual(self.obj.id, reloaded_obj.id)
        self.assertEqual(self.obj.name, reloaded_obj.name)

    def test_file_size(self):
        """Test file size after saving objects."""
        self.storage.new(self.obj)
        self.storage.save()
        file_size = os.path.getsize(self.file_path)
        self.assertGreater(file_size, 0)

if __name__ == '__main__':
    unittest.main()
