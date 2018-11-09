#!/usr/bin/python3
"""
This module contains unit tests for class BaseModel
"""
import unittest
import io
import sys
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """test for class BaseModel and its methods
    """
    def setUp(self):
        """Set up method"""
        self.base1 = BaseModel()
        self.base2 = BaseModel()

    def tearDown(self):
        """Tear down method"""
        pass

    def test_uuid(self):
        self.assertNotEqual(self.base1.id, self.base2.id)
        self.assertTrue(hasattr(self.base1, "id"))
        self.assertEqual(type(self.base1.id), str)
        self.assertEqual(type(self.base2.id), str)

    def test_instance(self):
        self.assertTrue(isinstance(self.base1, BaseModel))
        self.assertTrue(isinstance(self.base2, BaseModel))

    def test_created_at(self):
        self.assertTrue(hasattr(self.base1, "created_at"))
        self.assertEqual(type(self.base1.created_at), type(datetime.now()))
        self.assertNotEqual(self.base1.created_at, self.base2.created_at)

    def test_updated_at(self):
        self.assertTrue(hasattr(self.base1, "updated_at"))
        self.assertEqual(type(self.base1.updated_at), type(datetime.now()))
        self.assertNotEqual(self.base1.updated_at, self.base2.updated_at)

    def test_str(self):
        expected = "[{}] ({}) {}".format(
            self.base1.__class__.__name__,
            self.base1.id,
            self.base1.__dict__
        )
        a_io = io.StringIO()
        sys.stdout = a_io
        print(self.base1, end="")
        self.assertEqual(expected, a_io.getvalue())
        sys.stdout = sys.__stdout__

    def test_save(self):
        time = self.base1.updated_at
        self.base1.save()
        self.assertFalse(time == self.base1.updated_at)

#    def test_to_dict(self):
#        self.base1.name = "Holberton"
#        model_json = self.base1.to_dict()
#        base1_dict = self.base1.__dict__
#        self.assertEqual(model_json['created_at'], base1_dict['created_at'].isoformat())

if __name__ == '__main__':
    unittest.main()
