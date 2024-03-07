import unittest
from models.base_model import BaseModel
from datetime import datetime
from datetime import datetime, timedelta

class TestBaseModel(unittest.TestCase):

    def test_id_assignment(self):
        """Test if unique IDs are assigned correctly."""
        instance1 = BaseModel()
        instance2 = BaseModel()
        self.assertNotEqual(instance1.id, instance2.id)

    def test_datetime_assignment(self):
        instance = BaseModel()
        delta = instance.updated_at - instance.created_at
        self.assertTrue(delta < timedelta(seconds=1))

    def test_str_method(self):
        """Test the __str__ method format."""
        instance = BaseModel()
        expected_format = f"[BaseModel] ({instance.id}) {instance.__dict__}"
        self.assertEqual(instance.__str__(), expected_format)

    def test_to_dict_method(self):
        """Test the to_dict method."""
        instance = BaseModel()
        instance_dict = instance.to_dict()
        self.assertEqual(instance_dict['__class__'], 'BaseModel')
        self.assertEqual(instance_dict['id'], instance.id)
        self.assertIn('created_at', instance_dict)
        self.assertIn('updated_at', instance_dict)

    def test_save_method(self):
        """Test the save method updates 'updated_at'."""
        instance = BaseModel()
        old_updated_at = instance.updated_at
        instance.save()
        self.assertNotEqual(old_updated_at, instance.updated_at)

