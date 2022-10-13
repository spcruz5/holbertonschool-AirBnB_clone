#!/usr/bin/python3
""" Unittest for Amenity class """
import unittest
import json
import os
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.user import User
from models.engine.file_storage import FileStorage


class TestAmenity(unittest.TestCase):

    def setUp(self):
        """SetUp method"""
        self.amenity1 = Amenity()
        self.amenity1.name = "juan"

    def test_docstring(self):
        """test docstring in the file"""
        self.assertIsNotNone(Amenity.__doc__)

    def test_is_instance(self):
        """Test for instantiation"""
        self.assertIsInstance(self.amenity1, Amenity)
