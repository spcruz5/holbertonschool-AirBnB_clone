"""Defines unittests for models/engine/file_storage.py."""

import os
import json
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorage_init(unittest.TestCase):
    """Unittests for testing instantiation of the FileStorage class."""

    def test_FileStorage_instantiation_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_storage_initializes(self):
        self.assertEqual(type(models.storage), FileStorage)


class Test_File_Storage_Method(unittest.TestCase):
    """Test for the all method."""
    def test_all(self):
        """Check if it return a dictionary."""
        self.storage = FileStorage()
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        """Check if the object is in object."""
        self.storage = FileStorage()
        self.user = User()
        ob_dict = self.storage.all()
        key = "{}.{}".format(type(self.user).class_name, self.user.id)
        self.assertTrue(key in ob_dict.keys())

    def test_save(self):
        """Check the save method."""
        MyModel = BaseModel()
        self.storage = FileStorage()
        self.storage.save()
        self.path = self.storage._FileStoragefile_path
        with open(self.path) as file:
            file_dict = json.load(file)
        self.assertIn(MyModel.to_dict(), file_dict.values())

    def test_reload_method(self):
        """ Check the reload() method."""
        self.storage = FileStorage()
        MyModel = BaseModel()
        self.storage.save()
        self.storage.reload()
        key = "BaseModel.{}".format(MyModel.id)
        ob_dict = self.storage.all()
        self.assertFalse(ob_dict[key] is MyModel)
