#!/usr/bin/python3
import unittest
from models.engine.file_storage import FileStorage
from models.__init__ import storage
from models.base_model import BaseModel


class test_file_storage(unittest.TestCase):

    def setUp(self):
        """ Set a variable """
        self.my_model = BaseModel()
        self.fisto = FileStorage()

    def test_fiel_storage_exist(self):
        """ Check if methods exists """
        self.assertTrue(hasattr(self.fisto, "all"))
        self.assertTrue(hasattr(self.fisto, "new"))
        self.assertTrue(hasattr(self.fisto, "save"))
        self.assertTrue(hasattr(self.fisto, "reload"))

    def test_models_save(self):
        """ Check if the save function works """
        self.my_model.name = "Obi"
        self.my_model.save()
        storage.reload()
        storage.all()
        self.assertTrue(storage.all(), "Obi")
        self.assertTrue(hasattr(self.my_model, 'save'))
        self.assertNotEqual(self.my_model.created_at,
                            self.my_model.updated_at)

if __name__ == '__main__':
    unittest.main()