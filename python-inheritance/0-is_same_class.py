"""
0-is_same_class.py: Module containing a function to check if an object is exactly an instance of a specified class.
"""

def is_same_class(obj, a_class):
    """
    Check if an object is exactly an instance of a specified class.

    Args:
        obj (object): The object to be checked.
            It can be of any type.
        a_class (type): The class to compare against.
            It should be a Python class or a type.

    Returns:
        bool: True if obj is exactly an instance of a_class, otherwise False.
            Returns False if a_class is not a valid class or type.
    """
    return type(obj) is a_class
