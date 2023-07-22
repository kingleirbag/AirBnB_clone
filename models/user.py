#!/usr/bin/python3
from models.base_model import BaseModel

"""Class model of a User."""


class User(BaseModel):
    email = ""
    password = ""
    first_name = ""
    last_name = ""
