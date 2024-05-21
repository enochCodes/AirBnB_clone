#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
import unittest


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        """Set up test methods with the initial conditions needed."""
        storage.reload()

    def test_all_method(self):
        """Test that all method retrieves stored objects."""
        all_objs = storage.all()
        print("-- Reloaded objects --")
        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]
            print(obj)
            self.assertIsInstance(all_objs, dict)

    def test_create_new_object(self):
        """Test creation of a new BaseModel object."""
        print("-- Create a new object --")
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model.save()
        retrieved_objects = storage.all()
        self.assertIn(my_model.id, retrieved_objects)
        print(my_model)

    if __name__ == '__main__':
        unittest.main()
