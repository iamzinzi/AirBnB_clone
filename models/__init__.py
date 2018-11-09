#!/usr/bin/python3
"""
__init__.py
"""
from models.engine.file_storage import FileStorage

# __all__ = ["BaseModel"]
storage = FileStorage()
storage.reload()
