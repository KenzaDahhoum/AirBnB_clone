#!/usr/bin/python3
"""
This module defines the State class that inherits from BaseModel.
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    State class that holds state-specific information.
    """
    name = ""
