#!/usr/bin/python3
"""Unittest module for the Place Class."""

import unittest
from datetime import datetime
import time
from models.place import Place
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel

"""Test Cases for the Place class."""


class TestPlace(unittest.TestCase):
    def setUp(self):
        """Sets up test methods"""
        pass

    def tearDown(self):
        """Tears down test methods"""
        self.resetStorage()
        pass

    def resetStorage(self):
        """Reset FileStorage data"""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_place_model_instance(self):
        """Tests for instance of Place class."""
        place_model = Place()
        self.assertEqual(str(type(place_model)),
                         "<class 'models.place.Place'>")
        self.assertIsInstance(place_model, Place)
        self.assertTrue(issubclass(type(place_model), BaseModel))

    def test_place_model_attributes(self):
        """Tests the attributes of Place class."""
        attributes = storage.attributes()["Place"]
        place_model = Place()
        for key, val in attributes.items():
            self.assertTrue(hasattr(place_model, key))
            self.assertEqual(type(getattr(place_model, key, None)), val)


if __name__ == "__main__":
    unittest.main()
