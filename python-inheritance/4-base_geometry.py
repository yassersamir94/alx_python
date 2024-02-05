"""
4-base_geometry.py - Module containing the BaseGeometry class with an area() method.
"""

class BaseGeometry:
    """
    Base class representing geometry.

    This class serves as a base for other geometry-related classes.
    """

    __class__ = type

    def area(self):
        """
        Compute the area of the geometry.

        Raises:
            Exception: This method is not implemented in the base class.
        """
        raise Exception("area() is not implemented")
