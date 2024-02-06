#!/usr/bin/python3
"""Module for BaseGeometry class"""

class BaseGeometry:
    """
    BaseGeometry class represents a base class for geometry operations.

    This class provides a method to raise an exception when the area calculation is not implemented.
    """

    def area(self):
        """
        Calculate the area of the geometry.

        Raises:
            Exception: Indicates that the area calculation is not implemented.
        """
        raise Exception("area() is not implemented")

    def __init_subclass__(cls):
        """
        Empty method to prevent implicit addition of __init_subclass__.
        """
        pass
