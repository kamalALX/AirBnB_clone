#!/usr/bin/python3
""" teste file for console.py """
import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """this will test the console"""

    def test_help(self):
        """test if help works right"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
        output = "EOF  all  count  create  destroy  help  quit  show  update"
        self.assertTrue(output in f.getvalue())

    def test_create(self):
        """test if create works right"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            self.assertEqual(f.getvalue(), "** class name missing **\n")

    def test_quit(self):
        """test if quit works right"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
            self.assertTrue(f.getvalue() == "")

    def test_show(self):
        """test if show works right"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            self.assertTrue(f.getvalue() == "** class name missing **\n")

    def test_destroy(self):
        """test if destroy works right"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            self.assertTrue(f.getvalue() == "** class name missing **\n")

    def test_all(self):
        """test if all works right"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
            self.assertTrue(f.getvalue() != "")

    def test_count(self):
        """test if count works right"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count")
            self.assertEqual(f.getvalue(), "0\n")

    def test_update(self):
        """test if update works right"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update")
            self.assertTrue(f.getvalue() == "** class name missing **\n")

    def test_emptyline(self):
        """test if an empty line is handled properly"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("\n")
            self.assertTrue(f.getvalue() == "")


if __name__ == "__main__":
    unittest.main()
