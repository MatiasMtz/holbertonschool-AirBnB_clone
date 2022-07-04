#!/usr/bin/python3
"""
Unittest for Place class
"""

import unittest
from models.place import BaseModel
from models.place import Place


class test_place(unittest.TestCase):
    """
    Unittest for Place class
    """

    def test_place(self):
        """
        Test the instanitation of a new instance
        of Place and its methods
        """

        """
        Test if the class has a docstring
        """

        self.assertIsNotNone(Place.__doc__)

        """
        Instanitation
        """

        place = Place()
        update = place.updated_at

        self.assertEqual(isinstance(place, Place), True)
        self.assertEqual(issubclass(place.__class__, BaseModel), True)

        self.assertIsNotNone(place.city_id)
        self.assertEqual(type(place.city_id), str)
        self.assertEqual(place.city_id, "")
        self.assertIsNotNone(place.user_id)
        self.assertEqual(type(place.user_id), str)
        self.assertEqual(place.user_id, "")
        self.assertIsNotNone(place.name)
        self.assertEqual(type(place.name), str)
        self.assertEqual(place.name, "")
        self.assertIsNotNone(place.description)
        self.assertEqual(type(place.description), str)
        self.assertEqual(place.description, "")
        self.assertIsNotNone(place.number_rooms)
        self.assertEqual(type(place.number_rooms), int)
        self.assertEqual(place.number_rooms, 0)
        self.assertIsNotNone(place.number_bathrooms)
        self.assertEqual(type(place.number_bathrooms), int)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertIsNotNone(place.max_guest)
        self.assertEqual(type(place.max_guest), int)
        self.assertEqual(place.max_guest, 0)
        self.assertIsNotNone(place.price_by_night)
        self.assertEqual(type(place.price_by_night), int)
        self.assertEqual(place.price_by_night, 0)
        self.assertIsNotNone(place.latitude)
        self.assertEqual(type(place.latitude), float)
        self.assertEqual(place.latitude, 0.0)
        self.assertIsNotNone(place.longitude)
        self.assertEqual(type(place.longitude), float)
        self.assertEqual(place.longitude, 0.0)
        self.assertIsNotNone(place.amenity_ids)
        self.assertEqual(type(place.amenity_ids), list)
        self.assertEqual(place.amenity_ids, [])

        """
        str method
        """

        string = f"[Place] ({place.id}) {place.__dict__}"
        self.assertEqual(str(place), string)

        """
        save method
        """

        self.assertEqual(update, place.updated_at)
        place.save()
        self.assertNotEqual(update, place.updated_at)

        """
        to_dict method
        """

        test_dict = place.to_dict()
        self.assertEqual(type(test_dict), dict)
        self.assertEqual(type(test_dict["created_at"]), str)
        self.assertEqual(type(test_dict["updated_at"]), str)


if __name__ == '__main__':
    unittest.main()
