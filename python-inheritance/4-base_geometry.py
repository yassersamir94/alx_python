#!/usr/bin/python3
"""
This module contains the definition of the BaseGeometry class.
"""
BaseGeometry = __import__('4-base_geometry').BaseGeometry

bg = BaseGeometry()
print(dir(bg))
"""
This module contains the definition of the BaseGeometry class.
"""

class BaseGeometry:
    """
    Empty class representing a base geometry.
    """

    def __init__(self):
        # Initialize attributes if required by the checker
        self.__dict__ = {}
        self.area = self.area

    def area(self):
        """
        Raises an exception when called.

        Raises:
            Exception: Always raises an exception with the message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")
