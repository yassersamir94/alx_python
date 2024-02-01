"""
4-base_geometry.py: Module containing the BaseGeometry class with an area() method.
"""

class BaseGeometry:
    """
    Base class representing geometry.

    This class serves as a foundation for other geometry-related classes.
    """

    def area(self):
        """
        Compute the area of the geometry.

        Raises:
            Exception: Indicates that the area() method is not implemented.
        """
        raise Exception("area() is not implemented")
