#!/usr/bin/python3
import os
import json
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        """Set up initial conditions for tests."""
        self.storage = FileStorage()
        self.obj = BaseModel()
        self.obj.name = "Test Model"
        self.obj.my_number = 100
        self.file_path = FileStorage._FileStorage__file_path
        FileStorage._FileStorage__objects = {}
        self.storage.new(self.obj)  # Ensure the object is stored

    def tearDown(self):
        """Clean up after each test."""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        FileStorage._FileStorage__objects = {}

    def test_all_method(self):
        """Test that all method retrieves stored objects."""
        all_objs = self.storage.all()
        self.assertIsInstance(all_objs, dict)
        self.assertEqual(len(all_objs), 1)
        key = f"BaseModel.{self.obj.id}"
        self.assertIn(key, all_objs)
        self.assertEqual(all_objs[key].name, "Test Model")

    def test_save(self):
        """Test saving the objects to a file."""
        self.storage.save()
        self.assertTrue(os.path.exists(self.file_path))
        with open(self.file_path, 'r') as file:
            data = json.load(file)
            self.assertIn(f"BaseModel.{self.obj.id}", data)

    def test_reload(self):
        """Test reloading objects from a file."""
        self.storage.save()
        self.storage.reload()
        all_objs = self.storage.all()
        self.assertIn(f"BaseModel.{self.obj.id}", all_objs)


if __name__ == "__main__":
    unittest.main()
