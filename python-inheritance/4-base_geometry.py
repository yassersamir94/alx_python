#!/usr/bin/python3
"""Module for BaseGeometry class"""

class BaseGeometry:
    """
    Represents a class for base geometry with an area method.
    """

    def area(self):
        """
        Raises an Exception with a message indicating area is not implemented.
        """
        raise Exception("area() is not implemented")

    def __init_subclass__(cls):
        """
        Empty method to prevent implicit addition of __init_subclass__.
        """
        pass
