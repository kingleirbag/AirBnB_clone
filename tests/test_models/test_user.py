#!/usr/bin/python3
"""Unittest module for the User Class."""

import unittest
from datetime import datetime
import time
from models.user import User
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel

"""Test Cases for the User class."""


class TestUser(unittest.TestCase):
    def setUp(self):
        """Sets up test methods."""
        pass

    def tearDown(self):
        """Tears down test methods."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """Reset FileStorage data"""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_user_model_instance(self):
        """Tests for User class instance."""
        user_model = User()
        self.assertEqual(str(type(user_model)), "<class 'models.user.User'>")
        self.assertIsInstance(user_model, User)
        self.assertTrue(issubclass(type(user_model), BaseModel))

    def test_user_model_attributes(self):
        """Tests the attributes of User class."""
        attributes = storage.attributes()["User"]
        user_model = User()
        for key, val in attributes.items():
            self.assertTrue(hasattr(user_model, key))
            self.assertEqual(type(getattr(user_model, key, None)), val)


if __name__ == "__main__":
    unittest.main()
