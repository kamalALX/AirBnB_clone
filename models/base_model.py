#!/usr/bin/python3
""" """
import uuid
import datetime


class BaseModel():
    id = str(uuid.uuid4())
    created_at = datetime.datetime.now()
    updated_at = created_at

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        updated_at = datetime.datetime.now()

    def to_dict(self):
        diction = dict(self.__dict__)
        diction["__class__"] = self.__class__.__name__
        diction["created_at"] = self.created_at.isoformat()
        return diction
