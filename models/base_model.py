#!/usr/bin/python3
"""
Base class module
"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """class BaseModel"""
    def __init__(self):
        """Initializes instance of BaseModel class"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Prints a BaseModel Instance"""
        return "[{:s}] ({:s}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__
        )

    def save(self):
        """Updates the public instance attribute updated_at with the current
        datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__
        of the instance."""
        retval = self.__dict__
        retval['created_at'] = retval['created_at'].isoformat()
        retval['updated_at'] = retval['updated_at'].isoformat()
        retval['__class__'] = self.__class__.__name__
        return retval
