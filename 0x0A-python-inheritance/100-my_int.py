#!/usr/bin/python3
"""Defines a class MyInt that inherits from int.
"""


class MyInt(int):
    """Class MyInt inverts int operators == and !=.
    """

    def __eq__(self, value):
        """Override == opeartor with != behavior.
            Args:
                other: object to compare
            Returns: True if value and self are differents
                        False if otherwise
        """
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == behavior.
            Args:
                other: object to compare
            Returns: False if value and self are equal
                    True if otherwise
        """
        return self.real == value
