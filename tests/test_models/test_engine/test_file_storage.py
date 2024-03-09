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

    def test_all_returns_dict(self):
        """Test all method returns a dictionary"""
        all_objs = self.storage.all()
        self.assertIsInstance(all_objs, dict)

    def test_new_adds_to_all(self):
        """Test new method adds object to __objects"""
        obj = BaseModel()
        self.storage.new(obj)
        all_objs = self.storage.all()
        self.assertIn(f"{obj.__class__.__name__}.{obj.id}", all_objs)

    def test_new_with_no_object(self):
        """Test new method with no object"""
        initial_count = len(self.storage.all())
        self.storage.new(None)
        self.assertEqual(len(self.storage.all()), initial_count)

    def test_save(self):
        """Test save method"""
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.storage.new(obj1)
        self.storage.new(obj2)
        self.storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        all_objs = new_storage.all()
        self.assertIn(f"{obj1.__class__.__name__}.{obj1.id}", all_objs)
        self.assertIn(f"{obj2.__class__.__name__}.{obj2.id}", all_objs)

    def test_reload(self):
        """Test reload method"""
        obj1 = BaseModel()
        self.storage.new(obj1)
        self.storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        all_objs = new_storage.all()
        self.assertIn(f"{obj1.__class__.__name__}.{obj1.id}", all_objs)

    def test_reload_empty_file(self):
        """Test reload method with an empty file"""
        open(FileStorage._FileStorage__file_path, "w").close()
        new_storage = FileStorage()
        new_storage.reload()
        all_objs = new_storage.all()
        self.assertEqual(len(all_objs), 0)

    def test_reload_nonexistent_file(self):
        """Test reload method with a nonexistent file"""
        os.remove(FileStorage._FileStorage__file_path)
        new_storage = FileStorage()
        new_storage.reload()
        all_objs = new_storage.all()
        self.assertEqual(len(all_objs), 0)


if __name__ == "__main__":
    unittest.main()
