#!/usr/bin/python3
import unittest
from models.user import User
from models.place import Place


class TestUser(unittest.TestCase):
    """  """

    def setUp(self):
        """ initialization method """
        self.userObj = User()
        self.userObj.age = 26

    def testObjCreated(self):
        self.assertIsInstance(self.userObj, User)


if __name__ == '__main__':
    unittest.main()
