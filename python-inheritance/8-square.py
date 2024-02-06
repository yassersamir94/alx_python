#!/usr/bin/python3
"""
8-square.py - Module for the Square class.
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
        Initializes a Square instance.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self) -> str:
        """
        Returns a string representation of the square.

        Returns:
            str: A string representation of the square.
        """
        return "[Square] {}/{}".format(self.__width, self.__height)

    def area(self) -> Union[int, float]:
        """
        Computes the area of the square.

        Returns:
            int or float: The area of the square.
        """
        return self.__width * self.__height
