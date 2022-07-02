#!/usr/bin/python3
"""
Unit Test for BaseModel Class
"""
import unittest
from datetime import datetime
import models

BaseModel = models.base_model.BaseModel


class TestBaseModelInstances(unittest.TestCase):
    """testing for class instances"""

    def setUp(self):
        """creates a new instance for testing"""
        self.model = BaseModel()

    def test_instantiation(self):
        """checks if BaseModel is properly instantiated"""
        self.assertIsInstance(self.model, BaseModel)

    def test_save(self):
        """save function should update updated_at attribute"""
        self.model.save()
        actual = type(self.model.updated_at)
        expected = type(datetime.now())
        self.assertEqual(expected, actual)

    def test_name_attribute(self):
        """add name attribute"""
        self.model.name = "Holberton"
        actual = self.model.name
        expected = "Holberton"
        self.assertEqual(expected, actual)

    def test_number_attribute(self):
        """add number attribute"""
        self.model.number = 98
        actual = self.model.number
        self.assertTrue(98 == actual)


if __name__ == '__main__':
    unittest
