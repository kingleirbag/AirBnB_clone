#!/usr/bin/python3
"""Unittest module for the Review Class."""

import unittest
from datetime import datetime
import time
from models.review import Review
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel

"""Test Cases for the Review class."""


class TestReview(unittest.TestCase):

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

    def test_review_model_instance(self):
        """Tests for Review class instance"""
        review_model = Review()
        self.assertEqual(str(type(review_model)),
                         "<class 'models.review.Review'>")
        self.assertIsInstance(review_model, Review)
        self.assertTrue(issubclass(type(review_model), BaseModel))

    def test_attributes(self):
        """Tests for Review class attributes."""
        attributes = storage.attributes()["Review"]
        review_model = Review()
        for key, val in attributes.items():
            self.assertTrue(hasattr(review_model, key))
            self.assertEqual(type(getattr(review_model, key, None)), val)


if __name__ == "__main__":
    unittest.main()
