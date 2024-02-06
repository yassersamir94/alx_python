#!/usr/bin/python3
"""
6-rectangle.py - Module for the Rectangle class.
"""
BaseGeometry = __import__('5-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        Returns a string representation of the Rectangle.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    @property
    def width(self):
        """
        Retrieves the width of the Rectangle.

        Returns:
            int: The width of the Rectangle.
        """
        return self.__width

    @property
    def height(self):
        """
        Retrieves the height of the Rectangle.

        Returns:
            int: The height of the Rectangle.
        """
        return self.__height
