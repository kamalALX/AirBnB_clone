#!/usr/bin/python3
"""
Tests for FileStorage Class
"""
import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage"""

    @classmethod
    def setUpClass(cls):
        """Set up class for testing"""
        cls.storage = FileStorage()

    @classmethod
    def tearDownClass(cls):
        """Clean up class after testing"""
        try:
            os.remove(FileStorage._FileStorage__file_path)
        except FileNotFoundError:
            pass

    def test_all_returns_dict(self):
        """Test all method returns a dictionary"""
        all_objs = self.storage.all()
        self.assertIsInstance(all_objs, dict)

    def test_new(self):
        """Test new method"""
        obj = BaseModel()
        self.storage.new(obj)
        all_objs = self.storage.all()
        self.assertIn(f"{obj.__class__.__name__}.{obj.id}", all_objs)

    def test_save_reload(self):
        """Test save and reload methods"""
        obj1 = BaseModel()
        self.storage.new(obj1)
        self.storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        all_objs = new_storage.all()
        self.assertIn(f"{obj1.__class__.__name__}.{obj1.id}", all_objs)


if __name__ == "__main__":
    unittest.main()
