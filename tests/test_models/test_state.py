#!/usr/bin/python3
"""Unittest module for the State Class."""

import unittest
from datetime import datetime
import time
from models.state import State
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel

"""Test Cases for the State class."""


class TestState(unittest.TestCase):
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

    def test_state_model_instance(self):
        """Tests for instance of State class."""
        state_model = State()
        self.assertEqual(str(type(state_model)),
                         "<class 'models.state.State'>")
        self.assertIsInstance(state_model, State)
        self.assertTrue(issubclass(type(state_model), BaseModel))

    def test_attributes(self):
        """Tests for State class attributes."""
        attributes = storage.attributes()["State"]
        state_model = State()
        for key, val in attributes.items():
            self.assertTrue(hasattr(state_model, key))
            self.assertEqual(type(getattr(state_model, key, None)), val)


if __name__ == "__main__":
    unittest.main()
