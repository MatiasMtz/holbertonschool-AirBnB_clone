#!/usr/bin/python3
"""
Unittest for BaseModel class
"""

import unittest
from datetime import datetime
from models.base_model import BaseModel


class test_base_model(unittest.TestCase):
    """
    Unittest for BaseModel class
    """

    def test_docstring(self):
        """
        Test if the class has a docstring
        """

        self.assertIsNotNone(BaseModel.__doc__)

    def test_basemodel(self):
        """
        Test the instanitation of a new instance
        of base model and its methods
        """

        """
        Instanitation
        """

        base_model = BaseModel()
        update = base_model.updated_at
        self.assertEqual(isinstance(base_model, BaseModel), True)

        self.assertIsNotNone(base_model.id)
        self.assertIsNotNone(base_model.created_at)
        self.assertIsNotNone(base_model.updated_at)

        self.assertEqual(type(base_model.id), str)
        self.assertEqual(type(base_model.created_at), datetime)
        self.assertEqual(type(base_model.updated_at), datetime)

        """
        str method
        """

        string = f"[BaseModel] ({base_model.id}) {base_model.__dict__}"
        self.assertEqual(str(base_model), string)

        """
        save method
        """

        self.assertEqual(update, base_model.updated_at)
        base_model.save()
        self.assertNotEqual(update, base_model.updated_at)

        """
        to_dict method
        """

        test_dict = base_model.to_dict()
        self.assertEqual(type(test_dict), dict)
        self.assertEqual(type(test_dict["created_at"]), str)
        self.assertEqual(type(test_dict["updated_at"]), str)


if __name__ == '__main__':
    unittest.main()
