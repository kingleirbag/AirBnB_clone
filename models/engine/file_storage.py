#!/usr/bin/python3
import datetime
import json
import os

"""FileStorage Module Class"""


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Fetch all __objects dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """Create new object in the __objects dictionary."""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Save the __objects to JSON file."""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            all_objects = {key: obj.to_dict() for key, obj in FileStorage.
                           __objects.items()}
            json.dump(all_objects, f)

    def reload(self):
        """Fetch the JSON file to __objects."""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
            obj_dict = {
                key: self.classes()[obj["__class__"]](**obj)
                for key, obj in obj_dict.items()}
            FileStorage.__objects = obj_dict

    def classes(self):
        """Returns classes"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}
        return classes

    def attributes(self):
        """Returns classname and the attraibutes"""
        attributes = {
            "BaseModel":
                     {"id": str,
                      "created_at": datetime.datetime,
                      "updated_at": datetime.datetime},
            "User":
                     {"email": str,
                      "password": str,
                      "first_name": str,
                      "last_name": str},
            "State":
                     {"name": str},
            "City":
                     {"state_id": str,
                      "name": str},
            "Amenity":
                     {"name": str},
            "Place":
                     {"city_id": str,
                      "user_id": str,
                      "name": str,
                      "description": str,
                      "number_rooms": int,
                      "number_bathrooms": int,
                      "max_guest": int,
                      "price_by_night": int,
                      "latitude": float,
                      "longitude": float,
                      "amenity_ids": list},
            "Review":
            {"place_id": str,
                         "user_id": str,
                         "text": str}
        }
        return attributes
