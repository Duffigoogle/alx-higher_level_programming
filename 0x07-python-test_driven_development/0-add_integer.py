#!/usr/bin/python3
"""Add two integers"""


def add_integer(a, b=98):
    """
    Add two integers.
    Parameters:
        a: must be integer or float
        b: must be intefer or float
    Raise:
        TypeError: If a or b are not integers or floats
    Returns:
        Integer: The addition of a and b
    """
    if not (type(a) is int or type(a) is float):
        raise TypeError("a must be an integer")
    if not (type(b) is int or type(b) is float):
        raise TypeError("b must be an integer")
    if a+1 == a:
        raise OverflowError("a too large")
    if b+1 == b:
        raise OverflowError("b too large")

    return int(a) + int(b)
