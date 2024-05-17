#!/usr/bin/python3
"""
    user model
"""
from .base_model import BaseModel


class User(BaseModel):
    def __init__(self, first_name, last_name, passowrd):
        self.first_name = str(first_name)
        self.last_name = str(last_name)
        self.password = str(password)

