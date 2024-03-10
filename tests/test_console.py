import unittest
from unittest.mock import patch
from io import StringIO
import console
HBNBCommand = console.HBNBCommand
""" test """


class TestHBNBCommand(unittest.TestCase):
    """Test cases for the HBNBCommand console."""

    def test_quit_command(self):
        """Test the quit command exits the program."""
        with patch('sys.stdout', new_callable=StringIO) as _:
            with self.assertRaises(SystemExit):
                HBNBCommand().onecmd("quit")

    def test_EOF_command(self):
        """Test the EOF command exits the program."""
        with patch('sys.stdout', new_callable=StringIO) as _:
            with self.assertRaises(SystemExit):
                HBNBCommand().onecmd("EOF")

    def test_help_command(self):
        """Test the help command."""
        with patch('sys.stdout', new_callable=StringIO) as mock_output:
            HBNBCommand().onecmd("help")
            self.assertIn("Documented commands", mock_output.getvalue())

    def test_create_missing_class_name(self):
        """Test 'create' command with missing class name."""
        with patch('sys.stdout', new_callable=StringIO) as mock_output:
            HBNBCommand().onecmd("create")
            self.assertIn("** class name missing **", mock_output.getvalue())

    @patch('models.storage')
    def test_create_invalid_class_name(self, mock_storage):
        """Test 'create' command with invalid class name."""
        with patch('sys.stdout', new_callable=StringIO) as mock_output:
            HBNBCommand().onecmd("create MyClass")
            self.assertIn("** class doesn't exist **", mock_output.getvalue())


if __name__ == "__main__":
    unittest.main()
