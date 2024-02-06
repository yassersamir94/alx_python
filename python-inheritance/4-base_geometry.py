"""
This module contains the definition of the BaseGeometry class.
"""

class BaseGeometry:
    """
    Empty class representing a base geometry.
    """

    def area(self):
        """
        Raises an exception when called.

        Raises:
            Exception: Always raises an exception with the message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")
