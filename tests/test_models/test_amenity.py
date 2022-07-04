#!/usr/bin/python3
"""
Unittest for Amenity class
"""

import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class test_amenity(unittest.TestCase):
    """
    Unittest for Amenity class
    """

    def test_docstring(self):
        """
        Test if the class has a docstring
        """

        self.assertIsNotNone(Amenity.__doc__)

    def test_amenity(self):
        """
        Test the instanitation of a new instance
        of Amenity and its methods
        """
        """
        Instanitation
        """
        amenity = Amenity()
        update = amenity.updated_at

        self.assertEqual(isinstance(amenity, Amenity), True)
        self.assertEqual(issubclass(amenity.__class__, BaseModel), True)

        self.assertIsNotNone(amenity.name)
        self.assertEqual(type(amenity.name), str)
        self.assertEqual(amenity.name, "")

        """
        str method
        """

        string = f"[Amenity] ({amenity.id}) {amenity.__dict__}"
        self.assertEqual(str(amenity), string)

        """
        save method
        """

        self.assertEqual(update, amenity.updated_at)
        amenity.save()
        self.assertNotEqual(update, amenity.updated_at)

        """
        to_dict method
        """

        test_dict = amenity.to_dict()
        self.assertEqual(type(test_dict), dict)
        self.assertEqual(type(test_dict["created_at"]), str)
        self.assertEqual(type(test_dict["updated_at"]), str)


if __name__ == '__main__':
    unittest.main()
