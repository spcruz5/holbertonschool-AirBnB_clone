#!/usr/bin/python3
""" Unittest for State class """

import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):

    def setUp(self):
        """SetUp method"""
        self.state1 = State()
        self.state1.name = "juan"

    def test_docstring(self):
        """test docstring in the file"""
        self.assertIsNotNone(State.__doc__)

    def test_is_instance(self):
        """Test for instantiation"""
        self.assertIsInstance(self.state1, State)
