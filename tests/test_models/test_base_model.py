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
