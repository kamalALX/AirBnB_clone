#!/usr/bin/python3
""" teste file for console.py """
import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
import models
from models import storage


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
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            test_id = f.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as _:
            obj = models.storage.all()[f"BaseModel.{test_id}"]
            command = f"destroy BaseModel {test_id}"
            HBNBCommand().onecmd(command)
            self.assertNotIn(obj, models.storage.all())

    def test_destroy_objects_dot_notation(self):

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            test_id = f.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as _:
            obj = models.storage.all()[f"BaseModel.{test_id}"]
            command = f"BaseModel.destroy({test_id})"
            HBNBCommand().onecmd(command)
            self.assertNotIn(obj, models.storage.all())

    def test_create_object(self):

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            test_key = f"BaseModel.{f.getvalue().strip()}"
            self.assertIn(test_key, models.storage.all().keys())

    def test_show_missing_class(self):
        """Test behavior when class name is missing."""
        expected_output = "** class name missing **"

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show"))
            self.assertEqual(expected_output, output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(".show()"))
            self.assertNotEqual(expected_output, output.getvalue().strip())

    def test_show_invalid_class(self):
        """Test behavior when class doesn't exist."""
        expected_output = "** class doesn't exist **"

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show MyModel"))
            self.assertEqual(expected_output, output.getvalue().strip())

    def test_show_missing_id_space_notation(self):
        """Test behavior when instance id is missing (space notation)."""
        expected_output = "** instance id missing **"
        model_classes = ["BaseModel", "User", "State",
                         "City", "Amenity", "Place", "Review"]

        for model_class in model_classes:
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(f"show {model_class}"))
                self.assertEqual(expected_output, output.getvalue().strip())

    def test_destroy_invalid_class(self):
        correct = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy MyModel"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_destroy_id_missing_space_notation(self):
        correct = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy BaseModel"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_destroy_invalid_id_space_notation(self):
        correct = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy BaseModel 1"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_destroy_invalid_id_dot_notation(self):
        correct = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.destroy(1)"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_show_object_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            object_id = f.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd(f"show BaseModel {object_id}")
            self.assertIn(object_id, f.getvalue().strip())

    def test_show_object_dot_notation(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            object_id = f.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd(f"BaseModel.show({object_id})")
            self.assertIn(object_id, f.getvalue().strip())

    def test_update_object_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            object_id = f.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd(f"update BaseModel {object_id} name 'new_name'")
            self.console.onecmd(f"show BaseModel {object_id}")
            self.assertIn("new_name", f.getvalue().strip())

    def test_update_object_dot_notation(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            object_id = f.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd(f"BaseModel.update({object_id}, name='new_name')")
            self.console.onecmd(f"BaseModel.show({object_id})")
            self.assertIn("new_name", f.getvalue().strip())

    def test_HBNBCommand_class_docstring(self):
        self.assertIsNot(HBNBCommand.__doc__, None,
                         "HBNBCommand class needs a docstring")
        self.assertTrue(len(HBNBCommand.__doc__) >= 1,
                        "HBNBCommand class needs a docstring")


if __name__ == "__main__":
    unittest.main()
