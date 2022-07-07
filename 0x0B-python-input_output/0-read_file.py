#!/usr/bin/python3
"""Reading and writing"""


def read_file(filename=""):
    """reading operation
        Args:
            filename (str, optional): name of the text file. Defaults to "".
    """
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
