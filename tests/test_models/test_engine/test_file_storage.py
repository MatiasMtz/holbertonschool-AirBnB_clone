#!/usr/bin/python3
"""
Unittest for file_storage([..])
"""
import models
import os
import unittest
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity

F_storage = FileStorage()
B_model = BaseModel()
object = storage.all()


class TestFileStorage(unittest.TestCase):
    """ Write unittests for the class FileStorage. """
    def test_all(self):
        """ Test that checks the all method. """
        self.assertEqual(type(object), dict)
        self.assertTrue(hasattr(F_storage, 'all'), True)

    def test_new(self):
        """ Test that checks the new method. """
        B_model.name = 'Da_Sa'
        self.assertEqual(B_model.name, 'Da_Sa')
        self.assertTrue(hasattr(storage, 'new'), True)
        self.assertEqual(type(B_model), models.base_model.BaseModel)

    def test_save(self):
        """ Test that checks the save method. """
        self.assertTrue(hasattr(F_storage, 'save'), True)
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

    def test_no_objs(self):
        """
        check empty class
        """
        os.remove("file.json")
        FileStorage._FileStorage__objects = {}
        self.assertEqual(storage.all(), {})

    def test_save_create(self):
        """ Save  """
        obj = BaseModel()
        obj_key = 'BaseModel' + '.' + obj.id
        obj1 = User()
        obj1_key = 'User' + '.' + obj1.id
        obj2 = City()
        obj2_key = 'City' + '.' + obj2.id
        obj3 = Amenity()
        obj3_key = 'Amenity' + '.' + obj3.id
        obj4 = Place()
        obj4_key = 'Place' + '.' + obj4.id
        obj5 = Review()
        obj5_key = 'Review' + '.' + obj5.id
        obj6 = State()
        obj6_key = 'State' + '.' + obj6.id

        self.assertEqual(obj, storage.all()[obj_key])
        self.assertEqual(obj1, storage.all()[obj1_key])
        self.assertEqual(obj2, storage.all()[obj2_key])
        self.assertEqual(obj3, storage.all()[obj3_key])
        self.assertEqual(obj4, storage.all()[obj4_key])
        self.assertEqual(obj5, storage.all()[obj5_key])
        self.assertEqual(obj6, storage.all()[obj6_key])
       

if __name__ == '__main__':
    unittest.main()