#!/usr/bin/python3
"""Defines an inherited class checking function"""


def inherits_from(obj, a_class):
    """returns True if the object is an instance of
    a class that inherited (directly or indirectly)
    from the specified class
    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If the obj is an inherited instance of a_class - True.
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
