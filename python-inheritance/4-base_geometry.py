class BaseGeometry:
    """
    Base class representing geometry.

    This class serves as a base for other geometry-related classes.
    """

    def __init__(self):
        pass

    def area(self):
        """
        Compute the area of the geometry.

        Raises:
            Exception: This method is not implemented in the base class.
        """
        raise Exception("area() is not implemented")
