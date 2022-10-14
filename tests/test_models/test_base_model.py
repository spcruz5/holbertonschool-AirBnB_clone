#!/usr/bin/python3
""" Unittest for BaseModel class """

import unittest
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """Test class for BaseModel"""
    
    def setUp(self):
        """SetUp method"""
        self.bm_instance1 = BaseModel()
        self.bm_instance2 = BaseModel()
    
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

