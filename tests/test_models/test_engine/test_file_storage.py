#!/usr/bin/python3
""" tests for FileStorage Class """
import unittest
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage"""

    def setUp(self):
        """Set up for testing"""
        self.storage = FileStorage()

    def tearDown(self):
        """Clean up after testing"""
        try:
            os.remove(FileStorage._FileStorage__file_path)
        except FileNotFoundError:
            pass

    # def test_all(self):
    #     """Test all method"""
    #     all_objs = self.storage.all()
    #     self.assertEqual(type(all_objs), dict)

    # def test_new(self):
    #     """Test new method"""
    #     obj = BaseModel()
    #     self.storage.new(obj)
    #     all_objs = self.storage.all()
    #     self.assertIn("BaseModel." + obj.id, all_objs)

    def test_save_reload(self):
        """Test save and reload methods"""
        obj1 = BaseModel()
        obj2 = User()
        obj3 = State()
        self.storage.new(obj1)
        self.storage.new(obj2)
        self.storage.new(obj3)
        self.storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        all_objs = new_storage.all()
        self.assertIn("BaseModel." + obj1.id, all_objs)
        self.assertIn("User." + obj2.id, all_objs)
        self.assertIn("State." + obj3.id, all_objs)


if __name__ == "__main__":
    unittest.main()
