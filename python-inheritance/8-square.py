#!/usr/bin/python3
"""
Module 8-square.py - Defines the Square class.
"""

from typing import Union
Rectangle = __import__('7-rectangle').Rectangle

class Square(Rectangle):
    """
    Square class that inherits from Rectangle.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size: int):
        """
        Initializes a Square instance with a given size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self) -> str:
        """
        Returns a string representation of the Square object.

        Returns:
            str: A string representation of the Square object.
        """
        return "[Rectangle] {}/{}".format(self.__size, self.__size)

    def area(self) -> Union[int, float]:
        """
        Computes the area of the Square.

        Returns:
            Union[int, float]: The area of the Square.
        """
        return self.__size * self.__size
