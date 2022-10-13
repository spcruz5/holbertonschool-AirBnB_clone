#!/usr/bin/python3
""" Unittest for BaseModel class """
import unittest
import json
import os
from datetime import datetime
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.user import User
from models.engine.file_storage import FileStorage

class TestBaseModel(unittest.TestCase):
    """Test class for BaseModel"""
    def test_docstring(self):
        """test docstring in the file"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)
    
    def test_is_instance(self):
        """Test that instantiation is correct"""
        self.assertIsInstance(self.bm_instance1, BaseModel)
        self.assertIsInstance(self.bm_instance1.created_at, datetime)
        self.assertIsInstance(self.bm_instance1.updated_at, datetime)

