#!/usr/bin/python3
""" Unittest for City class """

import unittest
from models.city import City

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
