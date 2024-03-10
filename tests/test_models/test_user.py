#!/usr/bin/python3
import unittest
import os
from models import storage
from models.user import User
"""Test Script for User class functionality."""


class TestUser(unittest.TestCase):

    def setUp(self):
        """Delete file.json if it exists to ensure a fresh start."""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_user_creation(self):
        """Test the creation and persistence of User instances."""
        user1 = User()
        user1.first_name = "Betty"
        user1.last_name = "Holberton"
        user1.email = "betty.holberton@school.com"
        user1.password = "root"
        user1.save()

        user2 = User()
        user2.first_name = "John"
        user2.last_name = "Doe"
        user2.email = "john.doe@example.com"
        user2.password = "admin"
        user2.save()

        storage.reload()
        objects = storage.all()

        self.assertIn(f"User.{user1.id}", objects)
        self.assertIn(f"User.{user2.id}", objects)

        reloaded_user1 = objects[f"User.{user1.id}"]
        reloaded_user2 = objects[f"User.{user2.id}"]

        self.assertEqual(reloaded_user1.first_name, "Betty")
        self.assertEqual(reloaded_user1.last_name, "Holberton")
        self.assertEqual(reloaded_user1.email, "betty.holberton@school.com")
        self.assertEqual(reloaded_user1.password, "root")

        self.assertEqual(reloaded_user2.first_name, "John")
        self.assertEqual(reloaded_user2.last_name, "Doe")
        self.assertEqual(reloaded_user2.email, "john.doe@example.com")
        self.assertEqual(reloaded_user2.password, "admin")

    def tearDown(self):
        """Remove the file.json after the tests."""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass


if __name__ == '__main__':
    unittest.main()
