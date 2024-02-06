#!/usr/bin/python3
"""Module for BaseGeometry class"""


class BASEGEOMETRY:
    """Empty class BaseGeometry"""

    def area(self):
        """Raises an Exception with the message area() is not implemented"""
        raise Exception("area() is not implemented")

    def __init_subclass__(cls):
        """Empty method to prevent implicit addition of __init_subclass__"""
        pass

if __name__ == "__main__":
    # Code to execute when the script is run directly
    print("Running 4-base_geometry.py")
    bg = BaseGeometry()
    print(dir(bg))
