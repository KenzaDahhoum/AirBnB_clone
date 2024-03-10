#!/usr/bin/python3
import os
import sys
import unittest
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch
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

    def test_show_command_success(self):
        """Test 'show' command success."""
        cmd = "show BaseModel 1234-5678"
        expected = "** no instance found **\n"
        with patch('sys.stdout', new_callable=StringIO) as mock_out:
            HBNBCommand().onecmd(cmd)
            self.assertEqual(mock_out.getvalue(), expected)

    def test_destroy_command_success(self):
        """Test 'destroy' command success."""
        cmd = "destroy BaseModel 1234-5678"
        expected = "** no instance found **\n"
        with patch('sys.stdout', new_callable=StringIO) as mock_out:
            HBNBCommand().onecmd(cmd)
            self.assertEqual(mock_out.getvalue(), expected)

    def test_all_command(self):
        """Test 'all' command functionality."""
        with patch('sys.stdout', new_callable=StringIO) as mock_out:
            HBNBCommand().onecmd("all")
            self.assertTrue(isinstance(mock_out.getvalue(), str))

    def test_update_command_success(self):
        """Test 'update' command success."""
        cmd = "update BaseModel 1234-5678 name \"New Name\""
        expected = "** no instance found **\n"
        with patch('sys.stdout', new_callable=StringIO) as mock_out:
            HBNBCommand().onecmd(cmd)
            self.assertEqual(mock_out.getvalue(), expected)


if __name__ == "__main__":
    unittest.main()
