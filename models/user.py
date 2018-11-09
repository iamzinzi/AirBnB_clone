#!/usr/bin/python3
"""
User class module
"""
from models.base_model import BaseModel


class User(BaseModel):
    """class User which inherits from class BaseModel"""
    def __init__(self):
        """Initializes an instance of BaseModel"""
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
