#!/usr/bin/python3
"""1. Square with size
    A class to define a size of square.
"""


class Square:
    """Class that defines a square by:
        - Private instance attribute: size
        - Instantiation with size (no type/value verification)
    """

    def __init__(self, size):
        """Args:
        self: object instance.
        size (integer): size attribute passed..
        """
        self.__size = size
