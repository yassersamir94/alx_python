"""
2-inherits_from.py: Module containing a function to check if an object is an instance of a class
that inherited (directly or indirectly) from the specified class.
"""

def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class that inherited (directly or indirectly)
    from the specified class.

    Args:
        obj (object): The object to be checked.
            It can be of any type.
        a_class (type): The class to compare against.
            It should be a Python class or a type.

    Returns:
        bool: True if obj is an instance of a class that inherited from a_class, otherwise False.
            Returns False if a_class is not a valid class or type.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
