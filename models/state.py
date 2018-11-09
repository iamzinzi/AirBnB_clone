#!/usr/bin/python3
"""
State class module
"""
from models.base_model import BaseModel


class State(BaseModel):
    """class State which inherits from class BaseModel"""
    def __init__(self):
        """Initializes an instance of State"""
        self.name = ""
