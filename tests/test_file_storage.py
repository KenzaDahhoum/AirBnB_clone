import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):

    def setUp(self):
        """Set up method to start fresh."""
        FileStorage._FileStorage__objects = {}

    def test_all_method(self):
        """Test if all returns the dictionary correctly."""
        storage = FileStorage()
        self.assertEqual(len(storage.all()), 0)
        instance = BaseModel()
        storage.new(instance)
        self.assertEqual(len(storage.all()), 1)

    def test_new_method(self):
        """Test if new properly adds objects."""
        storage = FileStorage()
        instance = BaseModel()
        storage.new(instance)
        key = f"BaseModel.{instance.id}"
        self.assertIn(key, storage.all())

    def test_save_method(self):
        """Test if save properly serializes objects to file."""
        storage = FileStorage()
        instance = BaseModel()
        storage.new(instance)
        storage.save()
        self.assertTrue(os.path.exists(storage._FileStorage__file_path))

    def test_reload_method(self):
        """Test if reload properly deserializes objects from file."""
        storage = FileStorage()
        instance = BaseModel()
        storage.new(instance)
        storage.save()
        storage.reload()
        key = f"BaseModel.{instance.id}"
        self.assertIn(key, storage.all())

    def tearDown(self):
        """Tear down method to clean up after tests."""
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

