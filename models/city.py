#!/usr/bin/python3
"""
City class module
"""
from models.base_model import BaseModel


class City(BaseModel):
    """class City which inherits from BaseModel"""
    def __init__(self):
        """Initializes an instance of City"""
        self.state_id = ""
        self.name = ""
