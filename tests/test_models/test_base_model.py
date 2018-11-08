#!/usr/bin/python3
"""
This module contains unit tests for class BaseModel
"""
import unittest
import io, sys
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """test for class BaseModel and its methods
    """
    def setUp(self):
        """Set up method"""
        self.base_model = BaseModel()

    def tearDown(self):
        """Tear down method"""
        pass

    def test_attr_type(self):
        self.assertEqual(type(self.base_model.id), str)
        self.assertEqual(type(self.base_model.created_at), type(datetime.now()))
        self.assertEqual(type(self.base_model.updated_at), type(datetime.now()))

    def test_str(self):
        expected = "[{}] ({}) {}".format(
            self.base_model.__class__.__name__,
            self.base_model.id,
            self.base_model.__dict__
        )
        a_io = io.StringIO()
        sys.stdout = a_io
        print(self.base_model, end="")
        self.assertEqual(expected, a_io.getvalue())
        sys.stdout = sys.__stdout__

    def test_save(self):
        time = self.base_model.updated_at
        self.base_model.save()
        self.assertFalse(time == self.base_model.updated_at)

if __name__ == '__main__':
    unittest.main()
