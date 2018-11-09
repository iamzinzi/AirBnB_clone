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

    def test_attr_type(self):
        self.assertEqual(type(self.base1.id), str)
        self.assertEqual(type(self.base1.created_at), type(datetime.now()))
        self.assertEqual(type(self.base1.updated_at), type(datetime.now()))

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

if __name__ == '__main__':
    unittest.main()
