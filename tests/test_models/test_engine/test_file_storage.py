#!/usr/bin/python3
from datetime import datetime
import unittest
from time import sleep
import json
from models.engine.file_storage import FileStorage

"""Test for storage class model"""


class test_fileStorage(unittest.TestCase):
    """Test FileStorage Class"""
    def test_instances(self):
        """Test for storage instance"""
        obj = FileStorage()
        self.assertIsInstance(obj, FileStorage)

    def test_docs(self):
        """Test for save itemm"""
        self.assertIsNotNone(FileStorage.all)
        self.assertIsNotNone(FileStorage.new)
        self.assertIsNotNone(FileStorage.save)
        self.assertIsNotNone(FileStorage.reload)

    if __name__ == '__main__':
        unittest.main()
