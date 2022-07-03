#!/usr/bin/python3
"""Module for testing the file storage model"""
import json
import os
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test file storage class"""
    def test_creation(self):
        """Test creation of file storage and attributes"""
        new_fs = FileStorage()
        self.assertEqual(type(new_fs), FileStorage)
        """ not valid private attributes
        self.assertEqual(type(new_fs.__file_path), str)
        self.assertEqual(type(new_fs.__objects), dict)
        """

    def test_documentation(self):
        """Tests the documentation of file storage and methods"""
        new_fs = FileStorage()
        self.assertNotEqual(len(new_fs.__doc__), 0)
        self.assertNotEqual(len(new_fs.all.__doc__), 0)
        self.assertNotEqual(len(new_fs.new.__doc__), 0)
        self.assertNotEqual(len(new_fs.save.__doc__), 0)
        self.assertNotEqual(len(new_fs.reload.__doc__), 0)

    def test_methods(self):
        """Test methods of file storage model"""
        new_fs = FileStorage()
        """
    
        """
        new_bm = BaseModel()
        self.assertEqual(type(new_fs.all()), dict)
        self.assertNotEqual(len(new_fs.all()), 0)
        self.assertEqual(new_fs.new(new_bm), None)
        self.assertEqual(FileStorage.save(self), None)
        self.assertEqual(FileStorage.reload(self), None)

        aux_dict = new_fs.all()
        self.assertEqual(new_fs.new(BaseModel()), None)
        aux_dict2 = new_fs.all()

        self.assertEqual(new_fs.save(), None)
        self.assertEqual(new_fs.reload(), None)


    if __name__ == '__main__':
        unittest.main()