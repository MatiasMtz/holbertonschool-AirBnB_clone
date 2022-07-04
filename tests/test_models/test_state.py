#!/usr/bin/python3
"""
Unittest for State class
"""

import unittest
from models.base_model import BaseModel
from models.state import State


class test_state(unittest.TestCase):
    """
    Unittest for State class
    """

    def test_docstring(self):
        """
        Test if the class has a docstring
        """

        self.assertIsNotNone(State.__doc__)

    def test_state(self):
        """
        Test the instanitation of a new instance
        of State and its methods
        """
        """
        Instanitation
        """

        state = State()
        update = state.updated_at

        self.assertEqual(isinstance(state, State), True)
        self.assertEqual(issubclass(state.__class__, BaseModel), True)

        self.assertIsNotNone(state.name)
        self.assertEqual(type(state.name), str)
        self.assertEqual(state.name, "")

        """
        str method
        """

        string = f"[State] ({state.id}) {state.__dict__}"
        self.assertEqual(str(state), string)

        """
        save method
        """

        self.assertEqual(update, state.updated_at)
        state.save()
        self.assertNotEqual(update, state.updated_at)

        """
        to_dict method
        """

        test_dict = state.to_dict()
        self.assertEqual(type(test_dict), dict)
        self.assertEqual(type(test_dict["created_at"]), str)
        self.assertEqual(type(test_dict["updated_at"]), str)


if __name__ == '__main__':
    unittest.main()
