class BaseGeometry:
    """Empty class BaseGeometry"""

    def area(self):
        """Raises an Exception with the message area() is not implemented"""
        raise Exception("area() is not implemented")

    def __init_subclass__(cls):
        pass
