#!/usr/bin/python3
""" tests for FileStorage Class """
import unittest
import os
from models.base_model import BaseModel
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

    def test_all(self):
        """Test all method"""
        all_objs = self.storage.all()
        self.assertEqual(type(all_objs), dict)

    def test_new(self):
        """Test new method"""
        obj = BaseModel()
        self.storage.new(obj)
        all_objs = self.storage.all()
        self.assertIn("BaseModel." + obj.id, all_objs)

    def test_save_reload(self):
        """Test save and reload methods"""
        obj1 = BaseModel()
        self.storage.new(obj1)
        self.storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        all_objs = new_storage.all()
        self.assertIn("BaseModel." + obj1.id, all_objs)

    def test_reload_empty_file(self):
        """Test reload method with an empty file"""
        new_storage = FileStorage()
        new_storage.all().clear()
        new_storage.reload()
        all_objs = new_storage.all()
        self.assertEqual(len(all_objs), 0)

    def test_reload_nonexistent_file(self):
        """Test reload method with a nonexistent file"""
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

        new_storage = FileStorage()
        new_storage.reload()
        all_objs = new_storage.all()
        self.assertEqual(len(all_objs), 0)


if __name__ == "__main__":
    unittest.main()
