#!/usr/bin/python3
"""
Module for BaseGeometry class.

This module defines the BaseGeometry class, which serves as a base class
for geometry-related operations. It currently provides a method to raise
an exception when the area calculation is not implemented.
"""


class BaseGeometry:
    """Empty class BaseGeometry"""

    def area(self):
        """Raises an Exception with the message area() is not implemented"""
        raise Exception("area() is not implemented")

    def __init_subclass__(cls):
         """
        Empty method to override implicit addition of __init_subclass__.

        This method is empty to prevent Python from adding __init_subclass__
        implicitly to the class. It ensures that the output of dir(bg) does not
        include __init_subclass__.
        """
        pass
