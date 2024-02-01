def is_same_class(obj, a_class):
    """
    Check if an object is exactly an instance of a specified class.

    Args:
    - obj: object to be checked.
    - a_class: class to compare against.

    Returns:
    - True if obj is exactly an instance of a_class, otherwise False.
    """
    return type(obj) is a_class
