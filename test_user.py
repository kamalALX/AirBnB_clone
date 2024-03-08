#!/usr/bin/python3
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """  """

    def setUp(self):
        """ initialization method """
        self.userObj = User()
        self.userObj.age = 26

    def test_ObjCreated(self):
        self.assertIsInstance(self.userObj, BaseModel)
