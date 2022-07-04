#!/usr/bin/python3
"""
Unittest for User class
"""

import unittest
from models.base_model import BaseModel
from models.user import User


class test_user(unittest.TestCase):
    """
    Unittest for User class
    """

    def test_docstring(self):
        """
        Test if the class has a docstring
        """

        self.assertIsNotNone(User.__doc__)

    def test_review(self):
        """
        Test the instanitation of a new instance
        of User and its methods
        """
        """
        Instanitation
        """

        user = User()
        update = user.updated_at

        self.assertEqual(isinstance(user, User), True)
        self.assertEqual(issubclass(user.__class__, BaseModel), True)

        self.assertIsNotNone(user.email)
        self.assertEqual(type(user.email), str)
        self.assertEqual(user.email, "")
        self.assertIsNotNone(user.password)
        self.assertEqual(type(user.password), str)
        self.assertEqual(user.password, "")
        self.assertIsNotNone(user.first_name)
        self.assertEqual(type(user.first_name), str)
        self.assertEqual(user.first_name, "")
        self.assertIsNotNone(user.last_name)
        self.assertEqual(type(user.last_name), str)
        self.assertEqual(user.last_name, "")

        """
        str method
        """

        string = f"[User] ({user.id}) {user.__dict__}"
        self.assertEqual(str(user), string)

        """
        save method
        """

        self.assertEqual(update, user.updated_at)
        user.save()
        self.assertNotEqual(update, user.updated_at)

        """
        to_dict method
        """

        test_dict = user.to_dict()
        self.assertEqual(type(test_dict), dict)
        self.assertEqual(type(test_dict["created_at"]), str)
        self.assertEqual(type(test_dict["updated_at"]), str)


if __name__ == '__main__':
    unittest.main()
