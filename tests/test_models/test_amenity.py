#!/usr/bin/python3
""" Unittest for Amenity class """

import unittest
from models.amenity import Amenity


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
