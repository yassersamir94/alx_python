#!/usr/bin/python3
"""Module for BaseGeometry class"""
BaseGeometry = __import__('4-base_geometry').BaseGeometry

bg = BaseGeometry()
print(dir(bg))

class BaseGeometry:
    """
    Represents a class for base geometry with an area method.
    """

    def area(self):
        """
        Raises an Exception with a message indicating area is not implemented.
        """
        raise Exception("area() is not implemented")
