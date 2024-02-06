#!/usr/bin/python3
"""Module for Rectangle class"""


class BaseGeometry:
    """Empty class BaseGeometry"""

    def area(self):
        """Raises an Exception with the message area() is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value as an integer greater than 0"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Rectangle class inheriting from BaseGeometry"""

    def __init__(self, width, height):
        """Initializes Rectangle with width and height"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """Calculates the area of the Rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Returns the string representation of the Rectangle"""
        return f"[Rectangle] {self.__width}/{self.__height}"
