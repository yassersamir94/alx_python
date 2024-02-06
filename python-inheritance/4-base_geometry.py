#!/usr/bin/python3
"""
Module 4-base_geometry.py - Defines the BaseGeometry class.
"""


class BaseGeometry:
    """
    BaseGeometry class defines geometric operations.
    """

    def area(self):
        """
        Computes the area of the geometry.

        Raises:
            Exception: Always raises an exception with the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")

    def __dir__(self):
        """
        Customizes the dir() function to include only specific attributes.

        Returns:
            list: List of attribute names.
        """
        return ['__class__', 'area']
