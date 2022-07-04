#!/usr/bin/python3
"""
Unittest for FileStorage class
"""

import models
import os
import unittest
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


file_storage = FileStorage()
base_model = BaseModel()
object = storage.all()


class test_file_storage(unittest.TestCase):
    """ 
    Write unittests for the class FileStorage. """
    def test_all(self):
        """
        Test that checks the all method.
        """

        self.assertEqual(type(object), dict)
        self.assertTrue(hasattr(file_storage, 'all'), True)

    def test_new(self):
        """
        Test that checks the new method.
        """

        base_model.name = 'Betty'
        self.assertEqual(base_model.name, 'Betty')
        self.assertTrue(hasattr(storage, 'new'), True)
        self.assertEqual(type(base_model), models.base_model.BaseModel)

    def test_save(self):
        """
        Test that checks the save method.
        """

        self.assertTrue(hasattr(file_storage, 'save'), True)
        self.assertGreater(base_model.updated_at, base_model.created_at)

    def test_reload(self):
        """
        Test that checks the reload method.
        """

        self.assertTrue(hasattr(file_storage, 'reload'), True)

    def test_FileStorage_empty(self):
        """
        Test that checks the empty FileStorage.
        """

        self.assertIsNotNone(FileStorage.__doc__)
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_documentation(self):  
        """
        Tests for module, class, & method documentation.
        """

        self.assertTrue(len(FileStorage.__doc__) >= 1)
        self.assertTrue(len(FileStorage.all.__doc__) >= 1)
        self.assertTrue(len(FileStorage.new.__doc__) >= 1)
        self.assertTrue(len(FileStorage.save.__doc__) >= 1)
        self.assertTrue(len(FileStorage.reload.__doc__) >= 1)

    def test_no_objs(self):
        """
        Check empty class
        """

        os.remove("file.json")
        FileStorage._FileStorage__objects = {}
        self.assertEqual(storage.all(), {})
       

if __name__ == '__main__':
    unittest.main()