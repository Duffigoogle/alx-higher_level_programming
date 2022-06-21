#!/usr/bin/python3
"""2. Size validation
    A class to define a size of square
"""


class Square:
    """class Square that defines a square by:
        - Private instance attribute: size
        - Instantiation with optional size = 0
    """

    def __init__(self, size=0):
        """Args:
        self: object instance.
        size (integer): size of the square passed. Default size is 0.

        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """
        if type(size) != int:
            raise TypeError("Size must be an integer")

        if size < 0:
            raise ValueError("Size must be >= 0")
        self.__size = size
