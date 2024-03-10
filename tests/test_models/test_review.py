import unittest
from models.review import Review
""" test """


class TestReview(unittest.TestCase):

    def test_instance_creation(self):
        review = Review()
        self.assertIsInstance(review, Review)

    def test_attributes(self):
        review = Review()
        attrs = ['place_id', 'user_id', 'text']
        for attr in attrs:
            self.assertTrue(hasattr(review, attr))


if __name__ == "__main__":
    unittest.main()
