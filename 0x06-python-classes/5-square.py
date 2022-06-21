#!/usr/bin/python3
"""4. Access and update private attribute"""


class Square:
    """class Square that defines a square by:
        Private instance attribute: size:
            - property def size(self)
            - property setter def size(self, value)
        - Instantiation with optional size = 0
        Public instance method: def area(self).
        Public instance method: def my_print(self).
    """

    def __init__(self, size=0):
        """Args:
            self: object instance.
            size: size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """Returns:
            self.__size -- size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter of 'size' attribute
            Arguments:
                value {int} -- new size of the square
            Raises:
                TypeError: When value does not a int
                ValueError: When value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area
        """
        return self.__size * self.__size

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size > 0:
            for i in range(self.__size):
                print("#" * self.__size)
        else:
            print()
