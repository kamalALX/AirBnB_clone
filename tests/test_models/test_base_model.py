#!/usr/bin/python3
"""
Tests for BaseModel
"""
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """
    Tests for BaseModel
    """
    def setUp(self):
        """
        Test setUp
        """
        self.new_model = BaseModel()
        self.name = "Dennis McField"

    def test_obj(self):
        bmObj = BaseModel()


    def test_init(self):
        """
        Test init
        """

    def test_str(self):
        """
        Test str
        """

    def test_save(self):
        """
        Test save
        """

    def test_to_dict(self):
        """
        Test to_dict
        """

if __name__ == '__main__':
    unittest.main()
