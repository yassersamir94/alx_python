#!/usr/bin/python3
"""Module for Base class"""


class Base:
    """
    Base class for managing id attribute
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes Base instance with id attribute

        Args:
            id (int): Optional integer ID for the instance.
                      If not provided, it assigns an incremented value of __nb_objects.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
