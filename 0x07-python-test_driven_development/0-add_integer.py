#!/usr/bin/python3
"""Add two integers"""


def add_integer(a, b=98):
    """My addition function
    Parameters:
        a: first integer
        b: second integer which have a default value 98
    Raise:
        TypeError: If a or b are not integers or float
    Returns:
        The return value. a + b
    """

    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    elif type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)

    return a + b
