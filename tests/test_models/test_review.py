#!/usr/bin/python3
""" Unittest for Review class """


import unittest
from models.review import Review


class TestReview(unittest.TestCase):

    def setUp(self):
        """SetUp method"""
        self.review1 = Review()
        self.review1.place_id = "24g5gk2gk234"
        self.review1.user_id = "3r45t9s323d9"
        self.review1.text = "Loren ipsum"

    def test_docstring(self):
        """test docstring in the file"""
        self.assertIsNotNone(Review.__doc__)

    def test_is_instance(self):
        """Test for instantiation"""
        self.assertIsInstance(self.review1, Review)
