#!/usr/bin/python3
"""
This module contains the unittests for City class
"""
import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """
    Test for class City and its methods
    """
    def setUp(self):
        """
        Set up method
        """
        self.city1 = City()
        self.city2 = City()

    def tearDown(self):
        """
        Tear down method
        """
        pass

    def test_uuid(self):
        self.assertNotEqual(self.city1.id, self.city2.id)
        self.assertTrue(hasattr(self.city1, "id"))
        self.assertEqual(type(self.city1.id), str)

    def test_type(self):
        self.assertEqual(type(self.city1), City)
        self.assertEqual(type(self.city2), City)

    def test_state_id(self):
        self.assertTrue(hasattr(self.city1, "state_id"))
        self.assertTrue(type(self.city1.state_id) is str)
        self.assertEqual(self.city1.state_id, "")
        City.state_id = "California"
        self.assertEqual(self.city1.state_id, "California")
        self.assertEqual(self.city1.state_id, self.city2.state_id)
        self.city1.state_id = "New York"
        self.assertEqual(self.city1.state_id, "New York")
        self.assertFalse(self.city1.state_id == self.city2.state_id)

    def test_name(self):
        self.assertTrue(hasattr(self.city1, "name"))
        self.assertTrue(type(self.city1.name) is str)
        self.assertEqual(self.city1.name, "")
        City.name = "San Francisco"
        self.assertEqual(self.city1.name, "San Francisco")
        self.assertEqual(self.city1.name, self.city2.name)
        self.city1.name = "San Diego"
        self.assertEqual(self.city1.name, "San Diego")
        self.assertFalse(self.city1.name == self.city2.name)

    def test_isinstance(self):
        self.assertTrue(isinstance(self.city1, BaseModel))
        self.assertFalse(type(self.city1) is BaseModel)

    def test_init_with_kwargs(self):
        self.city1.name = "San Francisco"
        self.city1.state_id = "1234567890"
        model_json = self.city1.to_dict()
        my_new_city = City(**model_json)
        self.assertDictEqual(model_json, my_new_city.to_dict())
        self.assertIn("name", my_new_city.to_dict())
        self.assertEqual(my_new_city.name, "San Francisco")
        self.assertIsNot(self.city1, my_new_city)

if __name__ == '__main__':
    unittest.main()
