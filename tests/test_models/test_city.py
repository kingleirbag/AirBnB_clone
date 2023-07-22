#!/usr/bin/python3
"""Unittest module for the City Class."""

import unittest
from datetime import datetime
import time
from models.city import City
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel

"""Test Cases for the City class"""


class TestCity(unittest.TestCase):
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

    def test_city_model_attributes(self):
        """Tests the attributes of City class."""
        attributes = storage.attributes()["City"]
        city_model = City()
        for key, val in attributes.items():
            self.assertTrue(hasattr(city_model, key))
            self.assertEqual(type(getattr(city_model, key, None)), val)

    def test_city_model_instance(self):
        """Tests for instance of City class."""
        city_model = City()
        self.assertEqual(str(type(city_model)), "<class 'models.city.City'>")
        self.assertIsInstance(city_model, City)
        self.assertTrue(issubclass(type(city_model), BaseModel))


if __name__ == "__main__":
    unittest.main()
