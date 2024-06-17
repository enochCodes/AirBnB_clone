#!/usr/bin/python3
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_save(self):
        print("test BaseModel Save")
        my_model = BaseModel()
        my_model.save()
        my_model.name = "My First Model"
        my_model.my_number = 89
        print(my_model)
        my_model.save()
        print(my_model)
        my_model_json = my_model.to_dict()
        print(my_model_json)
        print("JSON of my_model:")
        for key in my_model_json.keys():
            print("\t{}: ({}) - {}".format(
                key, type(my_model_json[key]), my_model_json[key]
            ))

    def test_to_dict(self):
        ''' Test the to_dict method '''
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        model_dict = my_model.to_dict()
        self.assertEqual(model_dict['name'], "My_First_Model")
        self.assertEqual(model_dict['my_number'], 89)

if __name__ == "__main__":
    unittest.main()
