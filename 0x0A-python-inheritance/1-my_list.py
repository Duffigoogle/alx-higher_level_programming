#!/usr/bin/python3
"""Defines an inherited list class MyList."""


class MyList(list):
    """class MyList that inherits from list and implements sorting"""

    def print_sorted(self):
        """Public instance method that prints the sorted list in ascending order."""
        print(sorted(self))
