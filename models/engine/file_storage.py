#!/usr/bin/python3
""" """
import json
from models.base_model import BaseModel
from models.user import User


class_mapping = {
    "BaseModel": BaseModel,
    "User": User,
}

class FileStorage():
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        pass

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        formatted_dictionary = {}
        for key, obj in FileStorage.__objects.items():
            formatted_dictionary[key] = obj.to_dict()
        with open(FileStorage.__file_path, "w") as fileJSON:
            json.dump(formatted_dictionary, fileJSON, indent=4)

    def reload(self):
        try:
            new__objects = {}
            with open(FileStorage.__file_path, "r") as fileJSON:
                new__objects = json.load(fileJSON)
                for key, value in new__objects.items():
                    class_name = value["__class__"]
                    if class_name in class_mapping:
                        real_class = class_mapping[class_name]
                        obj = real_class(**value)
                        FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass

