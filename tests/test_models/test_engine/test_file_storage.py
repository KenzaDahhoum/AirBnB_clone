#!/usr/bin/python3

import os
import json
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
""" test file for storage """


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

    def test_new(self):
        bm = BaseModel()
        us = User()
        st = State()
        pl = Place()
        cy = City()
        am = Amenity()
        rv = Review()
        models.storage.new(bm)
        models.storage.new(us)
        models.storage.new(st)
        models.storage.new(pl)
        models.storage.new(cy)
        models.storage.new(am)
        models.storage.new(rv)
        self.assertIn("BaseModel." + bm.id, models.storage.all().keys())
        self.assertIn(bm, models.storage.all().values())
        self.assertIn("User." + us.id, models.storage.all().keys())
        self.assertIn(us, models.storage.all().values())
        self.assertIn("State." + st.id, models.storage.all().keys())
        self.assertIn(st, models.storage.all().values())
        self.assertIn("Place." + pl.id, models.storage.all().keys())
        self.assertIn(pl, models.storage.all().values())
        self.assertIn("City." + cy.id, models.storage.all().keys())
        self.assertIn(cy, models.storage.all().values())
        self.assertIn("Amenity." + am.id, models.storage.all().keys())
        self.assertIn(am, models.storage.all().values())
        self.assertIn("Review." + rv.id, models.storage.all().keys())
        self.assertIn(rv, models.storage.all().values())

    def test_new_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_save(self):
        bm = BaseModel()
        us = User()
        st = State()
        pl = Place()
        cy = City()
        am = Amenity()
        rv = Review()
        models.storage.new(bm)
        models.storage.new(us)
        models.storage.new(st)
        models.storage.new(pl)
        models.storage.new(cy)
        models.storage.new(am)
        models.storage.new(rv)
        models.storage.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + bm.id, save_text)
            self.assertIn("User." + us.id, save_text)
            self.assertIn("State." + st.id, save_text)
            self.assertIn("Place." + pl.id, save_text)
            self.assertIn("City." + cy.id, save_text)
            self.assertIn("Amenity." + am.id, save_text)
            self.assertIn("Review." + rv.id, save_text)

    def tearDown(self):
        """Tear down method to clean up after tests."""
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass
