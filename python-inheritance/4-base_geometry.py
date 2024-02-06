#!/usr/bin/python3
"""
This module defines the BaseGeometry class.
"""

class BaseGeometry:
    """
    A class representing geometric shapes.
    """

    def __getattribute__(self, name):
        """
        Retrieve an attribute.
        """
        return super().__getattribute__(name)

    def area(self):
        """
        Compute the area of the geometric shape.
        """
        raise Exception("area() is not implemented")
