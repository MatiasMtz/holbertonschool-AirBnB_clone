#!/usr/bin/python3
"""
Review class
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Class to represent the reviews
    """

    place_id = ""
    user_id = ""
    text = ""
