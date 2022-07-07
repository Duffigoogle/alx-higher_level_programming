#!/usr/bin/python3
"""Module for function is_same_class"""


def is_same_class(obj, a_class):
    """
    function that returns True if the object is exactly an instance
    of the specified class; otherwise False.
    Args:
        obj (Any): object to check
        a_class (type): type to check against
    Returns:
        [Boolean]: response
    """
    return type(obj) is a_class
