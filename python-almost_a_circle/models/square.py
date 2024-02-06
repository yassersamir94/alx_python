#!/usr/bin/python3
"""Module for Square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class, inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square instance.

        Args:
            size (int): Size of the square.
            x (int): X coordinate of the square's position.
            y (int): Y coordinate of the square's position.
            id (int): Optional ID for the square.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns a string representation of the Square instance."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )
