#!/usr/bin/python3
"""4. Append to a file"""


def append_write(filename="", text=""):
    """ appends a string at the end of a text file (UTF8)
    Args:
        filename (str, optional): text file name
        text (str, optional): must be string
    Returns:
        [int]: the number of characters added
    """
    with open(filename, mode='a', encoding='utf-8') as file:
        return file.write(text)
