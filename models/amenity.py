#!/usr/bin/python3
""" """
from models.base_model import BaseModel


class Amenity(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.name = ""
