#!/usr/bin/python3
""" """
import json


class FileStorage():
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        pass

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        """
        self.__objects[self.__class__.__name__.self.id] = obj
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        objectsJSON = {}
        for id, obj in FileStorage.__objects.items():
            if not isinstance(obj, dict):
                objectsJSON[id] = obj.to_dict()
            else:
                objectsJSON[id] = obj
        with open(FileStorage.__file_path, "w") as fileJSON:
            json.dump(objectsJSON, fileJSON, indent=4)

    def reload(self):
        try:
            with open(FileStorage.__file_path, "r") as fileJSON:
                FileStorage.__objects = json.load(fileJSON)
        except FileNotFoundError:
            pass

