#!/usr/bin/python3
""" """
import json


class FileStorage():
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        pass

    def all(self):
        return self.__objects

    def new(self, obj):
        """
        self.__objects[self.__class__.__name__.self.id] = obj
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        with open(FileStorage.__file_path, "a") as fileJSON:
            json.dump(FileStorage.__objects, fileJSON)

    def reload(self):
        try:
            with open(FileStorage.__file_path, "r") as fileJSON:
                FileStorage.__objects = json.load(fileJSON)
        except FileNotFoundError:
            pass

