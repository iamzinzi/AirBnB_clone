#!/usr/bin/python3
"""
This module contains unit tests for class BaseModel
"""
from datetime import datetime
import io
from models.base_model import BaseModel
from models.state import State
import sys
import unittest


class TestState(unittest.TestCase):
    """test for class State
    """
    def setUp(self):
        """Set up method"""
        self.state1 = State()
        self.state2 = State()

    def tearDown(self):
        """Tear down method"""
        pass

    def test_uuid(self):
        self.assertNotEqual(self.state1.id, self.state2.id)
        self.assertTrue(hasattr(self.state1, "id"))
        self.assertEqual(type(self.state1.id), str)
        self.assertEqual(type(self.state2.id), str)

    def test_instance(self):
        self.assertTrue(isinstance(self.state1, State))
        self.assertTrue(isinstance(self.state1, BaseModel))

    def test_type(self):
        self.assertEqual(type(self.state1), State)
