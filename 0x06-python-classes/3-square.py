#!/usr/bin/python3
"""3. Area of a square"""


class Square:
    """ a class to define and calculate the area of the square
    Args:
        - Private instance attribute: size
        - Instantiation with optional size = 0
        - Public instance method: def area(self).
    """

    def __init__(self, size=0):
        """initializing square
        Args:
            size (int): the size of the square passed. Defaults to 0.
        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """
        self.__size = size
        if type(self.__size) != int:
            raise TypeError('size must be an integer')
        elif self.__size < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        """ finding the area of the square
        Returns:
            int: the current square area.e
        """
        return self.__size ** 2
