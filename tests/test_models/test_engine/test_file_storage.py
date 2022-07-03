#!/usr/bin/python3
"""
Unittest for FileStorage class
"""

import unittest
from models import storage
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class FileStorage(unittest.TestCase):
    """
    Unittest for FileStorage clas
    """
    
    def test_docstring(self):
        """
        Test if the class has a docstring
        """
        self.assertIsNotNone(models.engine.file_storage.FileStorage.__doc__)
        self.assertIsNotNone(models.engine.file_storage.__doc__)
        self.assertIsNotNone(models.engine.file_storage.FileStorage.
                             all.__doc__)
        self.assertIsNotNone(models.engine.file_storage.FileStorage.
                             __init__.__doc__)
        self.assertIsNotNone(models.engine.file_storage.FileStorage.
                             new.__doc__)
        self.assertIsNotNone(models.engine.file_storage.FileStorage.
                             save.__doc__)
        self.assertIsNotNone(models.engine.file_storage.FileStorage.
                             reload.__doc__)

    def test_file_storage(self):
        """
        Test the instanitation of a new instance
        of User and its methods
        """

        file_storage = FileStorage()
        self.assertEqual(isinstance(file_storage, FileStorage), True)

        self.assertIsNotNone(models.engine.file_storage.FileStorage().all)
        self.assertIsNotNone(models.engine.file_storage.FileStorage().new)
        self.assertIsNotNone(models.engine.file_storage.FileStorage().save)
        self.assertIsNotNone(models.engine.file_storage.FileStorage().reload)
        self.assertIsNotNone(models.engine.file_storage.FileStorage().all())
        self.assertIsNotNone(models.storage.all())

if __name__ == '__main__':
    unittest.main()