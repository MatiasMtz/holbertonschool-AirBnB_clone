#!/usr/bin/python3
"""
Unittest for Review class
"""

import unittest
from models.base_model import BaseModel
from models.review import Review


class test_review(unittest.TestCase):
    """
    Unittest for Review class
    """

    def test_docstring(self):
        """
        Test if the class has a docstring
        """

        self.assertIsNotNone(Review.__doc__)

    def test_review(self):
        """
        Test the instanitation of a new instance
        of Review and its methods
        """
        """
        Instanitation
        """

        review = Review()
        update = review.updated_at

        self.assertEqual(isinstance(review, Review), True)
        self.assertEqual(issubclass(review.__class__, BaseModel), True)

        self.assertIsNotNone(review.place_id)
        self.assertEqual(type(review.place_id), str)
        self.assertEqual(review.place_id, "")
        self.assertIsNotNone(review.user_id)
        self.assertEqual(type(review.user_id), str)
        self.assertEqual(review.user_id, "")
        self.assertIsNotNone(review.text)
        self.assertEqual(type(review.text), str)
        self.assertEqual(review.text, "")

        """
        str method
        """

        string = f"[Review] ({review.id}) {review.__dict__}"
        self.assertEqual(str(review), string)

        """
        save method
        """

        self.assertEqual(update, review.updated_at)
        review.save()
        self.assertNotEqual(update, review.updated_at)

        """
        to_dict method
        """

        test_dict = review.to_dict()
        self.assertEqual(type(test_dict), dict)
        self.assertEqual(type(test_dict["created_at"]), str)
        self.assertEqual(type(test_dict["updated_at"]), str)


if __name__ == '__main__':
    unittest.main()
