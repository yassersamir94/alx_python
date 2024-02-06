#!/usr/bin/python3

class BaseGeometry:
    """
    This module defines the BaseGeometry class.

    Public Methods:
    - area(self): Raises an Exception with the message "area() is not implemented".
    """

    def area(self):
        """
        This method raises an Exception with the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")
