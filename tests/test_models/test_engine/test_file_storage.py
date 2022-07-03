#!/usr/bin/python3
"""
Unittest for file_storage([..])
"""
import models
import os.path
import unittest
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

F_storage = FileStorage()
B_model = BaseModel()
object = storage.all()


class TestFileStorage(unittest.TestCase):
    """ Write unittests for the class FileStorage. """
    def test_all(self):
        """ Test that checks the all method. """
        self.assertEqual(type(object), dict)
        self.assertTrue(hasattr(F_storage, 'all'), True)
        #self.assertIs(object, storage.FileStorageobjects)

    def test_new(self):
        """ Test that checks the new method. """
        B_model.name = 'Da_Sa'
        self.assertEqual(B_model.name, 'Da_Sa')
        self.assertTrue(hasattr(storage, 'new'), True)
        self.assertEqual(type(B_model), models.base_model.BaseModel)

    def test_save(self):
        """ Test that checks the save method. """
        self.assertTrue(os.path.isfile('file.json'))
        self.assertTrue(hasattr(F_storage, 'save'), True)
        self.assertEqual(os.path.isfile('file.json'), True)
        self.assertGreater(B_model.updated_at, B_model.created_at)

    def test_reload(self):
        """ Test that checks the reload method. """
        self.assertTrue(hasattr(F_storage, 'reload'), True)

    def test_FileStorage_empty(self):
        """ Test that checks the empty FileStorage. """
        self.assertIsNotNone(FileStorage.__doc__)
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_documentation(self):  
        """
        tests for module, class, & method documentation.
        """

        self.assertTrue(len(FileStorage.__doc__) >= 1)
        self.assertTrue(len(FileStorage.all.__doc__) >= 1)
        self.assertTrue(len(FileStorage.new.__doc__) >= 1)
        self.assertTrue(len(FileStorage.save.__doc__) >= 1)
        self.assertTrue(len(FileStorage.reload.__doc__) >= 1)


if __name__ == '__main__':
    unittest.main()