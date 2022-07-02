#!/usr/bin/python3
"""Amenity Test"""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test the Amenity module"""

    def test_class(self):
        """Test the amenity class"""
        self.assertEqual(Amenity.name, "")
        self.assertTrue(issubclass(Amenity, BaseModel))
