import unittest
from models.place import Place
""" test """


class TestPlace(unittest.TestCase):

    def test_instance_creation(self):
        place = Place()
        self.assertIsInstance(place, Place)

    def test_attributes(self):
        place = Place()
        attrs = ['city_id', 'user_id', 'name', 'description',
                 'number_rooms', 'number_bathrooms', 'max_guest',
                 'price_by_night', 'latitude', 'longitude', 'amenity_ids'
                 ]
        for attr in attrs:
            self.assertTrue(hasattr(place, attr))


if __name__ == "__main__":
    unittest.main()
