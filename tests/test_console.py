#!/usr/bin/python3
""" teste file for console.py """
import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
import models


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

    def test_destroy_objects_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            test_id = output.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as output:
            obj = models.storage.all()["BaseModel.{}".format(test_id)]
            command = "destroy BaseModel {}".format(test_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, models.storage.all())

        # Repeat the same structure for other models
        models_to_test = [
                "User", "State", "Place", "City", "Amenity", "Review"
                ]
        for model in models_to_test:
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(f"create {model}"))
                test_id = output.getvalue().strip()

            with patch("sys.stdout", new=StringIO()) as output:
                obj = models.storage.all()[f"{model}.{test_id}"]
                command = f"destroy {model} {test_id}"
                self.assertFalse(HBNBCommand().onecmd(command))
                self.assertNotIn(obj, models.storage.all())

    def test_destroy_objects_dot_notation(self):
        models_to_test = [
                "BaseModel", "User",
                "State", "City", "Amenity", "Place", "Review"
                ]

        for model in models_to_test:
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(f"create {model}"))
                test_id = output.getvalue().strip()

            with patch("sys.stdout", new=StringIO()) as output:
                obj = models.storage.all()[f"{model}.{test_id}"]
                command = f"{model}.destroy({test_id})"
                self.assertFalse(HBNBCommand().onecmd(command))
                self.assertNotIn(obj, models.storage.all())

    def test_create_object(self):
        models_to_test = [
                "BaseModel", "User", "State",
                "City", "Amenity", "Place", "Review"
                ]

        for model in models_to_test:
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(f"create {model}"))
                self.assertLess(0, len(output.getvalue().strip()))
                test_key = f"{model}.{output.getvalue().strip()}"
                self.assertIn(test_key, models.storage.all().keys())


if __name__ == "__main__":
    unittest.main()
