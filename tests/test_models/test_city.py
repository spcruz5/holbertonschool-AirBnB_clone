#!/usr/bin/python3
""" Unittest for City class """
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

class TestCity(unittest.TestCase):

    def setUp(self):
        """SetUp method"""
        self.city1 = City()
        self.city1.state_id = "ad45ad61as6d1"
        self.city1.name = "juan"

    def test_docstring(self):
        """test docstring in the file"""
        self.assertIsNotNone(City.__doc__)

    def test_is_instance(self):
        """Test for instantiation"""
        self.assertIsInstance(self.city1, City)
