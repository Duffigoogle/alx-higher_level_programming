#!/usr/bin/python3
"""12. Student to JSON with filter"""


class Student:
    """defines a student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance
        If attrs is a list of strings, only attribute names
        contained in this list must be retrieved.
        Otherwise, all attributes must be retrieved
        """
        new_dir = {}
        if type(attrs) is list:
            for key, value in self.__dict__.items():
                if key in attrs:
                    new_dir[key] = value
            return new_dir

        return self.__dict__
