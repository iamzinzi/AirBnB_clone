#!/usr/bin/python3
"""
Base class module
"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """class BaseModel"""
    def __init__(self, *args, **kwargs):
        """Initializes instance of BaseModel class"""
        if kwargs:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    setattr(self, k, datetime.strptime(
                        v,
                        "%Y-%m-%dT%H:%M:%S.%f"))
                elif k == '__class__':
                    continue
                else:
                    setattr(self, k, v)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Prints a BaseModel Instance"""
        return "[{:s}] ({:s}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__
        )

    def __repr__(self):
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
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__
        of the instance."""
        retval = (self.__dict__).copy()
        retval['created_at'] = retval['created_at'].isoformat()
        retval['updated_at'] = retval['updated_at'].isoformat()
        retval['__class__'] = self.__class__.__name__
        return retval
