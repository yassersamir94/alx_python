"""
1-is_kind_of_class.py: Module containing a function to check if an object is an instance of, or if it is an instance
of a class that inherited from, the specified class.
"""

def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of, or if it is an instance of a class that inherited from,
    the specified class.

    Args:
        obj (object): The object to be checked.
            It can be of any type.
        a_class (type): The class to compare against.
            It should be a Python class or a type.

    Returns:
        bool: True if obj is an instance of a_class or its subclass, otherwise False.
            Returns False if a_class is not a valid class or type.
    """
    return isinstance(obj, a_class)
