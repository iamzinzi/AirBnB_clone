#!/usr/bin/python3
"""
This module contains the unittest for the console.py file
"""
import unittest
import sys
import os
from io import StringIO
from unittest.mock import create_autospec
from console import HBNBCommand
from models import storage


class TestConsole(unittest.TestCase):
    """
    Test console.py
    """
    def setUp(self):
        self.mock_stdin = create_autospec(sys.stdin)
        self.mock_stdout = create_autospec(sys.stdout)
        self.cli = self.create()
        sys.stdout = StringIO()

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def create(self, server=None):
        return HBNBCommand(stdin=self.mock_stdin, stdout=self.mock_stdout)

    def _last_write(self, nr=None):
        if nr is None:
            return self.mock_stdout.write.call_args[0][0]
        return "".join(map(
            lambda x: x[0][0],
            self.mock_stdout.write.call_args_list[-nr:]))

    def test_quit(self):
        self.assertTrue(self.cli.onecmd("quit"))
        self.assertTrue(self.cli.onecmd("EOF"))

    def test_help(self):
        self.cli.onecmd("help help")
        string = "List available commands with \"help\" or detailed help with "
        string += "\"help cmd\".\n"
        self.assertEqual(string, self._last_write())
        self.cli.onecmd("help create")
        self.assertTrue(self._last_write())

    def test_create(self):
        self.cli.onecmd("create User")
        self.assertTrue(sys.stdout.getvalue())
        obj_id = "{}.{}".format("User", sys.stdout.getvalue())

if __name__ == '__main__':
    unittest.main()
