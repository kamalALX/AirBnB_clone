import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand

class TestConsole(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()
        self.console.prompt = ''

    def tearDown(self):
        pass

    @patch('sys.stdout', new_callable=StringIO)
    def test_help_command(self, mock_stdout):
        with patch('sys.stdin', side_effect=['EOF']):
            self.console.onecmd("help")
        output = mock_stdout.getvalue()
        self.assertTrue("Documented commands" in output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_quit_command(self, mock_stdout):
        with patch('sys.stdin', side_effect=['EOF']):
            self.console.onecmd("quit")
        output = mock_stdout.getvalue()
        self.assertEqual(output, "")

    # Add more test cases for other commands/features


if __name__ == '__main__':
    unittest.main()
