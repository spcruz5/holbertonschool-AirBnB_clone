#!/usr/bin/python3
""" Unittest for Place class """


import unittest
from models.place import Place



class TestPlace(unittest.TestCase):

    def setUp(self):
        """SetUp method"""
        self.place1 = Place()
        self.place1.city_id = "Barcelona"
        self.place1.user_id = "3r45t9s323d9"
        self.place1.name = "juan"
        self.place1.description = "Apartment"
        self.place1.number_rooms = 9
        self.place1.number_bathrooms = 5
        self.place1.max_guest = 36
        self.place1.price_by_night = 300
        self.place1.latitude = 43.6
        self.place1.longitude = 79.3
        self.place1.amenity_ids = ["d15s64sd", "4asdad"]

    def test_docstring(self):
        """test docstring in the file"""
        self.assertIsNotNone(Place.__doc__)

    def test_is_instance(self):
        """Test for instantiation"""
        self.assertIsInstance(self.place1, Place)
