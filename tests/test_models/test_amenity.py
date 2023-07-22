#!/usr/bin/python3
"""Unittest module for the Amenity Class."""

import unittest
from datetime import datetime
import time
from models.amenity import Amenity
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel

"""Test Cases for the Amenity class."""


class TestAmenity(unittest.TestCase):
    def setUp(self):
        """Sets up test methods."""
        pass

    def tearDown(self):
        """Tears down test methods."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """Reset FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_amenity_model_attributes(self):
        """Tests for valid attributes of Amenity class"""
        attributes = storage.attributes()["Amenity"]
        amenity = Amenity()
        for key, val in attributes.items():
            self.assertTrue(hasattr(amenity, key))
            self.assertEqual(type(getattr(amenity, key, None)), val)

    def test_amenity_model_instance(self):
        """Tests for instance amenity class."""
        amenity = Amenity()
        self.assertEqual(str(type(amenity)),
                         "<class 'models.amenity.Amenity'>")
        self.assertIsInstance(amenity, Amenity)
        self.assertTrue(issubclass(type(amenity), BaseModel))


if __name__ == "__main__":
    unittest.main()
