#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry.r"""


class BaseGeometry:
    """class based geometry"""

    def area(self):
        """Public instance method: that raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates 'value'
            Args:
                name [string] -- name of the parameter
                value [int] -- parameter to validate
            Raises:
                TypeError: if 'value' is not integer
                ValueError: if 'value' is less or equal to 0
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
