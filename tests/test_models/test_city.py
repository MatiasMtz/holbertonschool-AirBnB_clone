#!/usr/bin/python3
"""
Unittest for City class
"""

import unittest
from models.city import BaseModel
from models.city import City


class test_city(unittest.TestCase):
    """
    Unittest for City class
    """

    def test_city(self):
        """
        Test the instanitation of a new instance
        of City and its methods
        """

        """
        Test if the class has a docstring
        """

        self.assertIsNotNone(City.__doc__)

        """
        Instanitation
        """

        city = City()
        update = city.updated_at

        self.assertEqual(isinstance(city, City), True)
        self.assertEqual(issubclass(city.__class__, BaseModel), True)

        self.assertIsNotNone(city.name)
        self.assertEqual(type(city.name), str)
        self.assertEqual(city.name, "")
        self.assertIsNotNone(city.state_id)
        self.assertEqual(type(city.state_id), str)
        self.assertEqual(city.state_id, "")

        """
        str method
        """

        string = f"[City] ({city.id}) {city.__dict__}"
        self.assertEqual(str(city), string)

        """
        save method
        """

        self.assertEqual(update, city.updated_at)
        city.save()
        self.assertNotEqual(update, city.updated_at)

        """
        to_dict method
        """

        test_dict = city.to_dict()
        self.assertEqual(type(test_dict), dict)
        self.assertEqual(type(test_dict["created_at"]), str)
        self.assertEqual(type(test_dict["updated_at"]), str)


if __name__ == '__main__':
    unittest.main()
