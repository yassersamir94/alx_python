"""
This module contains the definition of the BaseGeometry class.
"""

class BaseGeometry:
    """
    Class representing a base geometry.

    Methods:
    - area(): Raises an Exception with the message 'area() is not implemented'.
    """
    def area(self):
        """
        Method to calculate the area of the geometry.
        
        Raises:
        - Exception: 'area() is not implemented'.
        """
        raise Exception('area() is not implemented')
