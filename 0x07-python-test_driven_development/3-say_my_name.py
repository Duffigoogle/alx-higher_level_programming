#!/usr/bin/python3
"""Say my name """


def say_my_name(first_name, last_name=""):
    """
        print name and last name
        Parameters:
            first_name (str): The first name
            last_name (str): The last name
        Raise:
            TypeError: if first or last name is not string
        Return: print My name is <first name> <last name>
        """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
