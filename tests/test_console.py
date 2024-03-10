import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestConsole(unittest.TestCase):

    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        pass

    def test_create_base_model(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            self.assertIn("created", f.getvalue().strip())

    def test_create_user(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            self.assertIn("created", f.getvalue().strip())

    def test_create_state(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create State")
            self.assertIn("created", f.getvalue().strip())

    def test_create_city(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create City")
            self.assertIn("created", f.getvalue().strip())

    def test_create_amenity(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create Amenity")
            self.assertIn("created", f.getvalue().strip())

    def test_create_place(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create Place")
            self.assertIn("created", f.getvalue().strip())

    def test_create_review(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create Review")
            self.assertIn("created", f.getvalue().strip())

    def test_show_base_model(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            output = f.getvalue().strip()
            object_id = output.split()[-1]
            self.console.onecmd(f"show BaseModel {object_id}")
            self.assertIn("BaseModel", f.getvalue().strip())

    def test_show_user(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            output = f.getvalue().strip()
            object_id = output.split()[-1]
            self.console.onecmd(f"show User {object_id}")
            self.assertIn("User", f.getvalue().strip())

    def test_show_state(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create State")
            output = f.getvalue().strip()
            object_id = output.split()[-1]
            self.console.onecmd(f"show State {object_id}")
            self.assertIn("State", f.getvalue().strip())

    def test_show_city(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create City")
            output = f.getvalue().strip()
            object_id = output.split()[-1]
            self.console.onecmd(f"show City {object_id}")
            self.assertIn("City", f.getvalue().strip())

    def test_show_amenity(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create Amenity")
            output = f.getvalue().strip()
            object_id = output.split()[-1]
            self.console.onecmd(f"show Amenity {object_id}")
            self.assertIn("Amenity", f.getvalue().strip())

    def test_show_place(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create Place")
            output = f.getvalue().strip()
            object_id = output.split()[-1]
            self.console.onecmd(f"show Place {object_id}")
            self.assertIn("Place", f.getvalue().strip())

    def test_show_review(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create Review")
            output = f.getvalue().strip()
            object_id = output.split()[-1]
            self.console.onecmd(f"show Review {object_id}")
            self.assertIn("Review", f.getvalue().strip())

    def test_destroy_base_model(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            output = f.getvalue().strip()
            object_id = output.split()[-1]
            self.console.onecmd(f"destroy BaseModel {object_id}")
            self.assertIn("destroyed", f.getvalue().strip())

    def test_destroy_user(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            output = f.getvalue().strip()
            object_id = output.split()[-1]
            self.console.onecmd(f"destroy User {object_id}")
            self.assertIn("destroyed", f.getvalue().strip())

    def test_destroy_state(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create State")
            output = f.getvalue().strip()
            object_id = output.split()[-1]
            self.console.onecmd(f"destroy State {object_id}")
            self.assertIn("destroyed", f.getvalue().strip())

    def test_destroy_city(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create City")
            output = f.getvalue().strip()
            object_id = output.split()[-1]
            self.console.onecmd(f"destroy City {object_id}")
            self.assertIn("destroyed", f.getvalue().strip())

    def test_destroy_amenity(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create Amenity")
            output = f.getvalue().strip()
            object_id = output.split()[-1]
            self.console.onecmd(f"destroy Amenity {object_id}")
            self.assertIn("destroyed", f.getvalue().strip())

    def test_destroy_place(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create Place")
            output = f.getvalue().strip()
            object_id = output.split()[-1]
            self.console.onecmd(f"destroy Place {object_id}")
            self.assertIn("destroyed", f.getvalue().strip())

    def test_destroy_review(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create Review")
            output = f.getvalue().strip()
            object_id = output.split()[-1]
            self.console.onecmd(f"destroy Review {object_id}")
            self.assertIn("destroyed", f.getvalue().strip())

    def test_all_base_model(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            self.console.onecmd("all BaseModel")
            self.assertIn("BaseModel", f.getvalue().strip())

    def test_all_user(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            self.console.onecmd("all User")
            self.assertIn("User", f.getvalue().strip())

    def test_all_state(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create State")
            self.console.onecmd("all State")
            self.assertIn("State", f.getvalue().strip())

    def test_all_city(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create City")
            self.console.onecmd("all City")
            self.assertIn("City", f.getvalue().strip())

    def test_all_amenity(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create Amenity")
            self.console.onecmd("all Amenity")
            self.assertIn("Amenity", f.getvalue().strip())

    def test_all_place(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create Place")
            self.console.onecmd("all Place")
            self.assertIn("Place", f.getvalue().strip())

    def test_all_review(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create Review")
            self.console.onecmd("all Review")
            self.assertIn("Review", f.getvalue().strip())

    def test_count_base_model(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            self.console.onecmd("count BaseModel")
            self.assertIn("1", f.getvalue().strip())

    def test_count_user(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            self.console.onecmd("count User")
            self.assertIn("1", f.getvalue().strip())

    def test_count_state(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create State")
            self.console.onecmd("count State")
            self.assertIn("1", f.getvalue().strip())

    def test_count_city(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create City")
            self.console.onecmd("count City")
            self.assertIn("1", f.getvalue().strip())

    def test_count_amenity(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create Amenity")
            self.console.onecmd("count Amenity")
            self.assertIn("1", f.getvalue().strip())

    def test_count_place(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create Place")
            self.console.onecmd("count Place")
            self.assertIn("1", f.getvalue().strip())

    def test_count_review(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create Review")
            self.console.onecmd("count Review")
            self.assertIn("1", f.getvalue().strip())

    def test_update_base_model(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            output = f.getvalue().strip()
            object_id = output.split()[-1]
            self.console.onecmd(f"update BaseModel {object_id} name 'new_name'")
            self.console.onecmd(f"show BaseModel {object_id}")
            self.assertIn("new_name", f.getvalue().strip())

    def test_update_user(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            output = f.getvalue().strip()
            object_id = output.split()[-1]
            self.console.onecmd(f"update User {object_id} name 'new_name'")
            self.console.onecmd(f"show User {object_id}")
            self.assertIn("new_name", f.getvalue().strip())

    def test_update_state(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create State")
            output = f.getvalue().strip()
            object_id = output.split()[-1]
            self.console.onecmd(f"update State {object_id} name 'new_name'")
            self.console.onecmd(f"show State {object_id}")
            self.assertIn("new_name", f.getvalue().strip())

    def test_update_city(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create City")
            output = f.getvalue().strip()
            object_id = output.split()[-1]
            self.console.onecmd(f"update City {object_id} name 'new_name'")
            self.console.onecmd(f"show City {object_id}")
            self.assertIn("new_name", f.getvalue().strip())

    def test_update_amenity(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create Amenity")
            output = f.getvalue().strip()
            object_id = output.split()[-1]
            self.console.onecmd(f"update Amenity {object_id} name 'new_name'")
            self.console.onecmd(f"show Amenity {object_id}")
            self.assertIn("new_name", f.getvalue().strip())

    def test_update_place(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create Place")
            output = f.getvalue().strip()
            object_id = output.split()[-1]
            self.console.onecmd(f"update Place {object_id} name 'new_name'")
            self.console.onecmd(f"show Place {object_id}")
            self.assertIn("new_name", f.getvalue().strip())

    def test_update_review(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create Review")
            output = f.getvalue().strip()
            object_id = output.split()[-1]
            self.console.onecmd(f"update Review {object_id} name 'new_name'")
            self.console.onecmd(f"show Review {object_id}")
            self.assertIn("new_name", f.getvalue().strip())


if __name__ == '__main__':
    unittest.main()
