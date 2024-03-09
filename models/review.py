#!/usr/bin/python3
"""
This module defines the Review class that inherits from BaseModel.
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class for storing review-specific information.
    """
    place_id = ""  # Place.id
    user_id = ""  # User.id
    text = ""
