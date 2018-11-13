#!/usr/bin/python3
"""
This module contains the tests for FileStorage class
"""
import unittest
import io
import sys
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestFileStorage(unittest.TestCase):
    """
    Test for class FileStorage and its methods
    """
    def setUp(self):
        """
        Set up method
        """
        # storage = models.engine.file_storage.FileStorage()
        pass

    def tearDown(self):
        """
        Tear down method
        """
        pass

    '''
    def test_file_path(self):
        self.assertEqual(self.storage.__file_path, "file.json")

    def test_objects(self):
        self.assertTrue(type(self.storage.__objects) is dict)
        self.assertTrue(self.storage.__object == False)
    '''
