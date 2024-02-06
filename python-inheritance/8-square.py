#!/usr/bin/python3
"""
Module 8-square.py - Defines the Square class.
"""

class Square:
    """
    Square class that represents a square shape.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size):
        """
        Initializes a Square instance with a given size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
        self.integer_validator("size", size)

    def __str__(self):
        """
        Returns a string representation of the Square object.

        Returns:
            str: A string representation of the Square object.
        """
        return "[Rectangle] {}/{}".format(self.__size, self.__size)

    def area(self):
        """
        Computes the area of the Square.

        Returns:
            int: The area of the Square.
        """
        return self.__size * self.__size

    def integer_validator(self, name, value):
        """
        Validates the value to be an integer and greater than 0.

        Args:
            name (str): The name of the value being validated.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
