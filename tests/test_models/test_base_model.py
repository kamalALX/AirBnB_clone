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
        self.new_model.name = "Dennis McField"

    def test_model(self):
        self.assertEqual(self.new_model.name, "Dennis McField")
        print(self.new_model.created_at)

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
