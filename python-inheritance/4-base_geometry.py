#!/usr/bin/python3
"""Module for BaseGeometry class"""

class BaseGeometry:
    """BaseGeometry class"""

    def __init_subclass__(cls):
        pass

    def area(self):
        """Calculate the area. This method raises an Exception as it is not implemented."""
        raise Exception("area() is not implemented")
