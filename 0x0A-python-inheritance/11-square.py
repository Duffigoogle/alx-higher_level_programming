#!/usr/bin/python3
"""Square Class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines a square class inheriting other class"""

    def __init__(self, size):
        """Instantiation, using integer_validator() to
        detect exceptions.
        Args:
            size [int] -- must be positive integer
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """returns the area of the rectangle"""
        return self.__size ** 2

    def __str__(self):
        """usage of __str__"""
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
