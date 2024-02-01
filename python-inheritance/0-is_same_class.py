def is_same_class(obj, a_class):
    """
    Check if an object is exactly an instance of a specified class.

    Args:
        obj (object): The object to be checked.
        a_class (type): The class to compare against.

    Returns:
        bool: True if obj is exactly an instance of a_class, otherwise False.
    """
    return type(obj) is a_class
