#!/usr/bin/python3
"""Module for BaseGeometry class"""


class BaseGeometry:
    """Empty class BaseGeometry"""

    def area(self):
        """Raises an Exception with the message area() is not implemented"""
        raise Exception("area() is not implemented")

if __name__ == "__main__":
    # Code to execute when the script is run directly
    print("Running 3-base_geometry.py")
    bg = BaseGeometry()
    print(dir(bg))
