#!/usr/bin/python3
"""
This module defines the City class that inherits from BaseModel.
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    City class for storing city-specific information.
    """
    state_id = ""
    name = ""
