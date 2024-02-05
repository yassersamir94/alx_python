"""
5-base_geometry.py - Module for the BaseGeometry class and its methods.

This module defines the BaseGeometry class and its methods:
    - area(self): Computes the area of the geometry (not implemented).
    - integer_validator(self, name, value): Validates an integer value.

Example:
    from 5-base_geometry import BaseGeometry

    bg = BaseGeometry()
    bg.integer_validator("my_int", 12)

"""

class BaseGeometry:
    """
    Base class representing geometry.

    This class serves as a base for other geometry-related classes.
    """

    def area(self):
        """
        Computes the area of the geometry.

        Raises:
            Exception: Indicates that the area() method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value as an integer.

        Args:
            name (str): The name of the value being validated.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
