import unittest
from models.state import State
""" test """


class TestState(unittest.TestCase):

    def test_instance_creation(self):
        state = State()
        self.assertIsInstance(state, State)

    def test_name_attribute(self):
        state = State()
        self.assertTrue(hasattr(state, 'name'))
        self.assertEqual(state.name, "")


if __name__ == "__main__":
    unittest.main()
