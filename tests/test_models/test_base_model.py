#!/usr/bin/python3
"""Unittest module for the BaseModel Class."""

from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime
import json
import os
import re
import time
import unittest
import uuid

"""Test Cases for the BaseModel class."""


class TestBaseModel(unittest.TestCase):
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

    def test_3_base_model_instance(self):
        """Tests for instance of BaseModel class."""
        base_model = BaseModel()
        self.assertEqual(str(type(base_model)),
                         "<class 'models.base_model.BaseModel'>")
        self.assertIsInstance(base_model, BaseModel)
        self.assertTrue(issubclass(type(base_model), BaseModel))

    def test_3_model_with_many_args(self):
        """Tests __init__ with many arguments."""
        self.resetStorage()
        args = [i for i in range(1000)]
        base_model = BaseModel(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        base_model = BaseModel(*args)

    def test_3_model_class_attributes(self):
        """Test attributes value for instance of a BaseModel class"""
        attributes = storage.attributes()["BaseModel"]
        base_model = BaseModel()
        for key, val in attributes.items():
            self.assertTrue(hasattr(base_model, key))
            self.assertEqual(type(getattr(base_model, key, None)), val)

    def test_3_model_created_at_and_update_at(self):
        """Tests created_at and updated_at are available"""
        date_now = datetime.now()
        base_model = BaseModel()
        diff = base_model.updated_at - base_model.created_at
        self.assertTrue(abs(diff.total_seconds()) < 0.01)
        diff = base_model.created_at - date_now
        self.assertTrue(abs(diff.total_seconds()) < 0.1)

    def test_base_model_id(self):
        """Tests for unique model's ids"""
        model_id = [BaseModel().id for i in range(1000)]
        self.assertEqual(len(set(model_id)), len(model_id))

    def test_base_model_save(self):
        """Tests the save method on the base model class"""
        base_model = BaseModel()
        time.sleep(0.5)
        date_now = datetime.now()
        base_model.save()
        diff = base_model.updated_at - date_now
        self.assertTrue(abs(diff.total_seconds()) < 0.01)

    def test_base_model_str(self):
        """Tests for __str__ method on the base model class"""
        base_model = BaseModel()
        regular_exp = re.compile(r"^\[(.*)\] \((.*)\) (.*)$")
        match_result = regular_exp.match(str(base_model))
        self.assertIsNotNone(match_result)
        self.assertEqual(match_result.group(1), "BaseModel")
        self.assertEqual(match_result.group(2), base_model.id)
        group_3 = match_result.group(3)
        group_3 = re.sub(r"(datetime\.datetime\([^)]*\))", "'\\1'", group_3)
        repaced_grp_3 = json.loads(group_3.replace("'", '"'))
        base_model_cpy = base_model.__dict__.copy()
        base_model_cpy["created_at"] = repr(base_model_cpy["created_at"])
        base_model_cpy["updated_at"] = repr(base_model_cpy["updated_at"])
        self.assertEqual(repaced_grp_3, base_model_cpy)

    def test_base_model_to_dict(self):
        """Tests for to_dict()  on the base model class"""
        base_model = BaseModel()
        base_model.name = "Gabriel"
        base_model.age = 30
        user = base_model.to_dict()
        self.assertEqual(user["id"], base_model.id)
        self.assertEqual(user["__class__"], type(base_model).__name__)
        self.assertEqual(user["created_at"], base_model.created_at.isoformat())
        self.assertEqual(user["updated_at"], base_model.updated_at.isoformat())
        self.assertEqual(user["name"], base_model.name)
        self.assertEqual(user["age"], base_model.age)

    def test_base_model_instance(self):
        """Tests for instance with **kwargs."""
        base_model = BaseModel()
        base_model.name = "ALX SE"
        base_model.my_number = 1232
        my_model_json = base_model.to_dict()
        my_new_model = BaseModel(**my_model_json)
        self.assertEqual(my_new_model.to_dict(), base_model.to_dict())

    def test_base_model_instance_with_custom_dict(self):
        """Tests for instance with **kwargs from custom dict."""
        custom_dict = {"__class__": "BaseModel",
                       "updated_at":
                           datetime(2050, 12, 30, 23,
                                    59, 59, 123456).isoformat(),
                           "created_at": datetime.now().isoformat(),
                           "id": uuid.uuid4(),
                           "var": "foobar",
                           "int": 108,
                           "float": 3.14}
        base_model = BaseModel(**custom_dict)
        self.assertEqual(base_model.to_dict(), custom_dict)

    def test_base_model_instance_save(self):
        """Tests that model save"""
        self.resetStorage()
        base_model = BaseModel()
        base_model.save()
        key = "{}.{}".format(type(base_model).__name__, base_model.id)
        obj = {key: base_model.to_dict()}
        self.assertTrue(os.path.isfile(FileStorage._FileStorage__file_path))
        with open(FileStorage._FileStorage__file_path,
                  "r", encoding="utf-8") as f:
            self.assertEqual(len(f.read()), len(json.dumps(obj)))
            f.seek(0)
            self.assertEqual(json.load(f), obj)


if __name__ == '__main__':
    unittest.main()
