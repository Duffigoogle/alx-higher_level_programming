#!/usr/bin/python3
""" Print square """


def print_square(size):
    """
        prints a square with the character #
        Parameters:
            size: must be an integer (is the size of the square)
        Raises:
            TypeError: if size is not integer
            ValueError: If size is less than 0
        """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        print('#' * size)
