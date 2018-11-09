#!/usr/bin/python
"""
Amenity class module
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """class Amenity which inherits from BaseModel"""
    def __init__(self):
        """Initializes an instance of Amenity"""
        self.name = ""
